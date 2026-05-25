"""Выборочный экспорт ключевых Markdown в DOCX/PDF (Pandoc + Marp), без сборки всего сайта MkDocs."""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPORTS = ROOT / "exports"


@dataclass(frozen=True)
class ExportItem:
    source: Path
    docx_name: str | None = None
    marp_pdf_name: str | None = None
    marp_pptx_name: str | None = None


# Только важные материалы — не весь каталог analogs (128 файлов)
MANIFEST: list[ExportItem] = [
    ExportItem("docs/README.md", docx_name="01-glavnaya-dokumentaciya.docx"),
    ExportItem("docs/grant/README.md", docx_name="02-materialy-granta.docx"),
    ExportItem(
        "docs/presentations/grant-presentation.md",
        marp_pdf_name="prezentaciya-grant.pdf",
        marp_pptx_name="prezentaciya-grant.pptx",
    ),
    ExportItem(
        "docs/analogs/grant174-pobediteli/analiz-pobediteli.md",
        docx_name="analiz-pobediteli-grant174.docx",
        marp_pdf_name="analiz-pobediteli-grant174.pdf",
    ),
]


def _which(name: str) -> str | None:
    return shutil.which(name)


def _strip_marp_frontmatter(text: str) -> str:
    if not text.startswith("---"):
        return text
    match = re.match(r"^---\s*\n.*?\n---\s*\n", text, re.DOTALL)
    return text[match.end() :] if match else text


def _run(cmd: list[str], *, what: str) -> None:
    print(f"  > {' '.join(cmd)}")
    subprocess.run(cmd, check=True, cwd=ROOT)


def _pandoc_to_docx(src: Path, dst: Path, pandoc: str) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    body = _strip_marp_frontmatter(src.read_text(encoding="utf-8"))
    tmp = EXPORTS / "_tmp" / f"{src.stem}.md"
    tmp.parent.mkdir(parents=True, exist_ok=True)
    tmp.write_text(body, encoding="utf-8")
    _run(
        [
            pandoc,
            str(tmp),
            "-f",
            "markdown",
            "-t",
            "docx",
            "-o",
            str(dst),
        ],
        what="pandoc",
    )


def _marp_export(src: Path, dst: Path, marp: str, fmt: str) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    flag = "--pdf" if fmt == "pdf" else "--pptx"
    _run([marp, str(src), flag, "-o", str(dst), "--allow-local-files"], what="marp")


def _export_structure_docx() -> Path | None:
    script = ROOT / "scripts" / "build_grant_structure_docx.py"
    if not script.is_file():
        return None
    subprocess.run([sys.executable, str(script)], check=True, cwd=ROOT)
    src = ROOT / "docs" / "grant" / "Структура_проекта_грант_СВО_Чебаркуль.docx"
    if not src.is_file():
        return None
    dst = EXPORTS / "03-struktura-proekta.docx"
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    print(f"  > copy {src.name} -> {dst}")
    return dst


def main() -> int:
    EXPORTS.mkdir(parents=True, exist_ok=True)
    pandoc = _which("pandoc")
    marp = _which("marp")

    print(f"Папка экспорта: {EXPORTS}")
    if not pandoc:
        print("WARN: pandoc не найден в PATH — DOCX не будут созданы.")
        print("      Установка: https://pandoc.org/installing.html")
    if not marp:
        print("WARN: marp не найден в PATH — PDF/PPTX слайдов не будут созданы.")
        print("      npm install -g @marp-team/marp-cli")

    ok = 0
    for item in MANIFEST:
        src = ROOT / item.source
        if not src.is_file():
            print(f"SKIP (нет файла): {item.source}")
            continue
        print(f"\n[{item.source}]")
        if item.docx_name and pandoc:
            _pandoc_to_docx(src, EXPORTS / item.docx_name, pandoc)
            ok += 1
        if item.marp_pdf_name and marp:
            _marp_export(src, EXPORTS / item.marp_pdf_name, marp, "pdf")
            ok += 1
        if item.marp_pptx_name and marp:
            _marp_export(src, EXPORTS / item.marp_pptx_name, marp, "pptx")
            ok += 1

    print("\n[Структура проекта DOCX]")
    if _export_structure_docx():
        ok += 1

    readme = EXPORTS / "README.txt"
    readme.write_text(
        "Сгенерировано scripts/export_documents.py\n"
        "DOCX: Pandoc | PDF/PPTX слайдов: Marp\n"
        "PDF из DOCX: откройте в Word → Сохранить как PDF\n",
        encoding="utf-8",
    )

    print(f"\nГотово. Файлов обработано: {ok}. Смотрите папку exports/")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
