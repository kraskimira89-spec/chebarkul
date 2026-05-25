# Chebarkul Grant Project

**Психологическая и гуманитарная помощь участникам СВО**  
Грант Губернатора Челябинской области · рабочая документация · май 2026

---

## О проекте

Регулярные **выездные миссии** в тыловые районы (полигоны, подразделения) с мягкой психологической поддержкой, первичной диагностикой, гуманитарным сопровождением и **навигацией к помощи** после возвращения домой.

| | |
|---|---|
| **Рабочее название** | «Крепкий тыл — ближе победа» |
| **Целевая группа** | Участники СВО на передышке; при возвращении — жители Челябинской области |
| **Формат** | 1 выезд в месяц, 10–14 дней; команда 4–7 человек + партнёры |
| **Договор-образец** | № 89-26-1-000205 («НейроПульс») |

---

## Быстрые ссылки

| Раздел | Описание |
|--------|----------|
| [Материалы гранта](grant/README.md) | Договор PDF, ТЗ, структура проекта |
| [Договор (PDF)](grant/dogovor.md) | Просмотр договора в браузере |
| [Техническое задание](grant/tz.md) | ТЗ в HTML |
| [Структура проекта](grant/struktura-proekta.md) | Полная структура заявки |
| [Презентация](presentations/grant-presentation.md) | Слайды для экспертов (Marp) |
| [Экспорт PDF/PPTX](presentations/README.md) | Команды Marp CLI |

---

## Презентация для гранта

Готовые слайды: [grant-presentation.md](presentations/grant-presentation.md) — проблема, ЦГ, решение, команда, результаты, календарь.

**Экспорт:**

```powershell
python -m chebarkul_grant build-docs
marp docs/presentations/grant-presentation.md --pdf -o assets/presentations/grant-presentation.pdf
```

Подробнее: [presentations/README.md](presentations/README.md).

**Все ключевые документы в DOCX/PDF (выборочно, не весь сайт):**

```powershell
python -m chebarkul_grant export-docs
```

Инструкция: [export-guide.md](export-guide.md).

---

## Локальный просмотр

```powershell
.\.venv\Scripts\Activate.ps1
python -m chebarkul_grant build-docs
mkdocs serve
```

Если `mkdocs` не распознан — используйте `.\.venv\Scripts\mkdocs.exe serve` или `.\scripts\serve-docs.ps1`.

Публичный сайт: **https://kraskimira89-spec.github.io/chebarkul/**

---

## Прочие разделы

- `reports/` — промежуточные и итоговые отчёты (по мере готовности)
- `assets/audio/` — аудиозаписи рабочих встреч

Перед `mkdocs serve` обновите страницы гранта: `python -m chebarkul_grant build-docs`.
