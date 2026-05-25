# Чебаркуль: грантовый проект

Рабочий репозиторий для подготовки материалов гранта, документации, презентаций, изображений и вспомогательных скриптов.

## Быстрый старт

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -U pip
python -m pip install -e ".[dev,docs,ai]"
Copy-Item .env.example .env   # при первом запуске
pytest
ruff check .
```

Репозиторий: [github.com/kraskimira89-spec/chebarkul](https://github.com/kraskimira89-spec/chebarkul.git)

## Структура

- `src/chebarkul_grant/` - исходный код и автоматизация проекта.
- `docs/` - документация, материалы гранта и презентации.
- `assets/` - изображения, презентации и другие медиафайлы.
- `scripts/` - одноразовые и служебные скрипты.
- `tests/` - тесты.

## Документация в браузере

```powershell
python scripts/build_mkdocs_grant_pages.py
mkdocs serve
```

Откройте разделы **Договор (PDF)** и **Техническое задание** в меню сайта.
