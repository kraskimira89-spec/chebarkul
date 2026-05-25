# Запуск MkDocs из виртуального окружения проекта
$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root

$mkdocs = Join-Path $Root ".venv\Scripts\mkdocs.exe"
$python = Join-Path $Root ".venv\Scripts\python.exe"

if (-not (Test-Path $mkdocs)) {
    Write-Error "Не найден $mkdocs. Выполните: .\.venv\Scripts\pip install -e `".[docs]`""
}

& $python scripts\build_mkdocs_grant_pages.py
& $mkdocs serve @args
