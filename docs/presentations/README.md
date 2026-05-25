# Презентации

## Просмотр в браузере

Страница [grant-presentation.md](grant-presentation.md) в MkDocs — это слайды в формате Marp (разделители `---`).

## Экспорт в PDF и PPTX

Установите [Marp CLI](https://github.com/marp-team/marp-cli):

```powershell
npm install -g @marp-team/marp-cli
```

Из корня проекта:

```powershell
marp docs/presentations/grant-presentation.md --pdf -o assets/presentations/grant-presentation.pdf
marp docs/presentations/grant-presentation.md --pptx -o assets/presentations/grant-presentation.pptx
```

Или через расширение **Marp for VS Code** / Cursor: открыть `grant-presentation.md` → экспорт из палитры команд.

После изменения текста презентации пересоберите PDF/PPTX.
