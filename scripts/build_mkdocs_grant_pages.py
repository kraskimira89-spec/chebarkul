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

# Стили Word, которые mammoth по умолчанию не распознаёт
DOCX_STYLE_MAP = """
p[style-name='Title'] => h1:fresh
p[style-name='Heading 1'] => h1:fresh
p[style-name='Heading 2'] => h2:fresh
p[style-name='Heading 3'] => h3:fresh
"""


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


def _message_text(message: object) -> str:
    return str(getattr(message, "message", message))


def _important_messages(messages: list[object]) -> list[str]:
    """Скрыть шумные предупреждения о неизвестных стилях абзацев Word."""
    ignored_fragment = "Unrecognised paragraph style:"
    return [text for msg in messages if ignored_fragment not in (text := _message_text(msg))]


def _convert_docx_to_html(docx_path: Path) -> mammoth.results.Result:
    with docx_path.open("rb") as docx_file:
        return mammoth.convert_to_html(docx_file, style_map=DOCX_STYLE_MAP)


def build_docx_page(*, docx_filename: str, output_md: str, title: str) -> None:
    docx_path = GRANT / docx_filename
    if not docx_path.is_file():
        raise FileNotFoundError(f"Не найден файл: {docx_path}")

    result = _convert_docx_to_html(docx_path)

    docx_href = _grant_href(docx_filename)
    notes = _important_messages(result.messages)
    warnings = "\n".join(f"- {note}" for note in notes)
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
