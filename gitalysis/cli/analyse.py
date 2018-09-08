import sys
import click
from gitalizer.extensions import logger

from gitalysis.analysis import (
    analyse_travel_path,
    analyse_punch_card,
)


@click.group()
def analyse():
    """DB subcommand base."""
    pass


# ----- Analysis -------
@click.command()
@click.option('--existing/-e', default=False)
def travel(existing):
    """Analyse missing time stuff."""
    try:
        analyse_travel_path(existing)
    except KeyboardInterrupt:
        logger.info("CTRL-C Exiting Gracefully")
        sys.exit(1)


@click.command()
@click.option('--existing/-e', default=False)
def punchcard(existing):
    """Analyse missing time stuff."""
    try:
#            for method in ['mean-shift', 'dbscan', 'affinity']:
        for method in ['affinity']:
            if method == 'dbscan':
                for min_samples in range(5, 10, 5):
                    for eps in range(140, 150, 2):
                        analyse_punch_card(
                            existing, method,
                            eps=eps, min_samples=min_samples,
                        )
            else:
                analyse_punch_card(existing, method)
    except KeyboardInterrupt:
        logger.info("CTRL-C Exiting Gracefully")
        sys.exit(1)


analyse.add_command(travel)
analyse.add_command(punchcard)
