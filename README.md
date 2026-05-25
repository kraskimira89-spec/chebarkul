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
python -m chebarkul_grant build-docs
python -m chebarkul_grant version
mkdocs serve
```

Откройте разделы **Договор (PDF)**, **Техническое задание**, **Структура проекта** и **Презентация** в меню сайта. Экспорт слайдов в PDF/PPTX: `docs/presentations/README.md`.

## Публикация на GitHub Pages

Документация публикуется автоматически при push в ветку `main` (workflow `.github/workflows/docs.yml`).

**Один раз в настройках репозитория GitHub:** Settings → Pages → Build and deployment → Source: **GitHub Actions**.

Сайт: https://kraskimira89-spec.github.io/chebarkul/
