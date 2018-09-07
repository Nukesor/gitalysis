"""Cli for gitalysis."""
import click
from .analyse import analyse
from .plot import plot


@click.group()
def cli():
    """Init function for gitalizer."""
    pass


cli.add_command(analyse)
cli.add_command(plot)
