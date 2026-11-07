<!-- source: https://raw.githubusercontent.com/danielgatis/rembg/main/rembg/commands/d_command.py, fetched 2026-11-07, http 200, rendered with Playwright -->
import click

from ..bg import download\_models

@click.command(  # type: ignore
    name="d",
    help="download models",
)
@click.argument("models", nargs=-1)
def d\_command(models: tuple\[str, ...\]) -> None:
    """
    Download models
    """
    download\_models(models)
