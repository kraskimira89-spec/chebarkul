# Выборочный экспорт DOCX/PDF (Pandoc + Marp)
$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root

$python = Join-Path $Root ".venv\Scripts\python.exe"
if (-not (Test-Path $python)) {
    Write-Error "Не найден $python"
}

& $python scripts\build_mkdocs_grant_pages.py
& $python scripts\export_documents.py
