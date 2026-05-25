# 2026-05-24: Создание структуры проекта

Создан стандартный каркас Python-проекта для грантовой разработки:

- добавлен `src`-layout с пакетом `chebarkul_grant`;
- добавлены папки `docs`, `assets`, `tests`, `.cursor`, `.github`, `.vscode`;
- добавлены зависимости для документов, презентаций, изображений и AI-интеграций;
- добавлены настройки Ruff, pytest, mypy, MkDocs, pre-commit и CI;
- добавлен шаблон презентации Marp.

## 2026-05-24 (вечер): завершение настройки

- материалы гранта перенесены в `docs/grant/`, аудио — в `assets/audio/`;
- скрипт `build_grant_structure_docx.py` пишет в `docs/grant/` относительно корня;
- git init, 2 коммита, push в https://github.com/kraskimira89-spec/chebarkul.git (ветка `main`);
- pre-commit установлен; pytest и ruff проходят.
