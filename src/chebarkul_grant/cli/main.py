from pathlib import Path

import typer

from chebarkul_grant import __version__

app = typer.Typer(help="CLI для грантового проекта Чебаркуля.")


@app.command("version")
def print_version() -> None:
    """Показать версию проекта."""
    typer.echo(__version__)


@app.command("build-docs")
def build_docs() -> None:
    """Сгенерировать страницы MkDocs для договора и ТЗ."""
    import subprocess
    import sys

    script = Path(__file__).resolve().parents[3] / "scripts" / "build_mkdocs_grant_pages.py"
    subprocess.run([sys.executable, str(script)], check=True)


@app.command("export-docs")
def export_docs() -> None:
    """Экспорт ключевых MD в DOCX/PDF (Pandoc + Marp) в папку exports/."""
    import subprocess
    import sys

    root = Path(__file__).resolve().parents[3]
    mkdocs_script = root / "scripts" / "build_mkdocs_grant_pages.py"
    export_script = root / "scripts" / "export_documents.py"
    subprocess.run([sys.executable, str(mkdocs_script)], check=True)
    subprocess.run([sys.executable, str(export_script)], check=True)


def main() -> None:
    app()
