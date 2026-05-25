"""Генерация страниц MkDocs для просмотра материалов гранта в браузере."""

from __future__ import annotations

from pathlib import Path
from urllib.parse import quote

import mammoth

ROOT = Path(__file__).resolve().parents[1]
GRANT = ROOT / "docs" / "grant"

PDF_NAME = "89-26-1-000205 Договор о предоставлении гранта.pdf"
DOCX_TZ = "TZ.docx"
DOCX_STRUCTURE = "Структура_проекта_грант_СВО_Чебаркуль.docx"


def _grant_href(filename: str) -> str:
    """URL от корня сайта MkDocs (работает из любой вложенной страницы)."""
    return f"/grant/{quote(filename)}"


def build_dogovor_page() -> None:
    pdf_href = _grant_href(PDF_NAME)
    content = f"""# Договор о предоставлении гранта

[Скачать PDF]({pdf_href})

<iframe
  src="{pdf_href}"
  title="Договор о предоставлении гранта"
  style="width:100%;height:80vh;border:1px solid var(--md-default-fg-color--lightest);"
></iframe>
"""
    (GRANT / "dogovor.md").write_text(content, encoding="utf-8")


def build_docx_page(*, docx_filename: str, output_md: str, title: str) -> None:
    docx_path = GRANT / docx_filename
    if not docx_path.is_file():
        raise FileNotFoundError(f"Не найден файл: {docx_path}")

    with docx_path.open("rb") as docx_file:
        result = mammoth.convert_to_html(docx_file)

    docx_href = _grant_href(docx_filename)
    warnings = "\n".join(f"- {msg}" for msg in result.messages)
    warn_block = f'\n\n!!! warning "Замечания при конвертации"\n\n{warnings}\n' if warnings else ""

    content = f"""# {title}

[Скачать DOCX]({docx_href})
{warn_block}
<div class="grant-docx" markdown="0">

{result.value}

</div>
"""
    (GRANT / output_md).write_text(content, encoding="utf-8")


def main() -> None:
    pdf_path = GRANT / PDF_NAME
    if not pdf_path.is_file():
        raise FileNotFoundError(f"Не найден файл: {pdf_path}")

    build_dogovor_page()
    build_docx_page(docx_filename=DOCX_TZ, output_md="tz.md", title="Техническое задание")
    build_docx_page(
        docx_filename=DOCX_STRUCTURE,
        output_md="struktura-proekta.md",
        title="Структура проекта",
    )
    print(
        "MkDocs pages: docs/grant/dogovor.md, docs/grant/tz.md, " "docs/grant/struktura-proekta.md"
    )


if __name__ == "__main__":
    main()
