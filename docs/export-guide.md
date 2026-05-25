# Экспорт в Word и PDF (выборочно)

Не весь сайт MkDocs, а **только ключевые материалы** — через Pandoc (DOCX) и Marp (PDF/PPTX слайдов).

## Что нужно установить

| Инструмент | Назначение | Установка |
|------------|------------|-----------|
| **Pandoc** | Markdown → DOCX | https://pandoc.org/installing.html |
| **Marp CLI** | Слайды → PDF/PPTX | `npm install -g @marp-team/marp-cli` |

## Одна команда

```powershell
.\.venv\Scripts\Activate.ps1
python -m chebarkul_grant export-docs
```

Или:

```powershell
.\scripts\export-docs.ps1
```

## Что попадает в папку `exports/`

| Файл | Источник |
|------|----------|
| `01-glavnaya-dokumentaciya.docx` | `docs/README.md` |
| `02-materialy-granta.docx` | `docs/grant/README.md` |
| `03-struktura-proekta.docx` | скрипт `build_grant_structure_docx.py` |
| `prezentaciya-grant.pdf` / `.pptx` | `docs/presentations/grant-presentation.md` |
| `analiz-pobediteli-grant174.docx` / `.pdf` | `docs/analogs/.../analiz-pobediteli.md` |

Папка `exports/` в `.gitignore` — для локальной отправки и печати.

## PDF из Word (лучшее качество для русского текста)

1. Откройте `.docx` из `exports/` в Word.
2. **Файл → Сохранить как → PDF**.

## Добавить свой файл в экспорт

Отредактируйте список `MANIFEST` в `scripts/export_documents.py`.

## Почему не mkdocs-with-pdf

Плагин собирает **весь сайт** в один PDF — долго, тяжёлый файл, неудобно для гранта. Выборочный Pandoc/Marp даёт отдельные аккуратные документы.
