import typer

from chebarkul_grant import __version__

app = typer.Typer(help="CLI для грантового проекта Чебаркуля.")


@app.callback()
def main() -> None:
    """Корневая группа команд CLI."""


@app.command()
def version() -> None:
    """Показать версию проекта."""
    typer.echo(__version__)
