import sys
import click
from gitalizer.extensions import logger
from gitalizer.plot import (
    plot_user,
    plot_employee,
    plot_comparison,
)


@click.group()
def plot():
    """DB subcommand base."""
    pass


@click.command()
@click.argument('login')
def user(login):
    """Plot all graphs for a specific github user."""
    try:
        plot_user(login)
    except KeyboardInterrupt:
        logger.info("CTRL-C Exiting Gracefully")
        sys.exit(1)


@click.command()
@click.argument('login')
@click.argument('repositories', nargs=-1)
def user_for_repositories(login, repositories):
    """Get statistics of an user for specific repositories."""
    try:
        plot_employee(login, repositories)
    except KeyboardInterrupt:
        logger.info("CTRL-C Exiting Gracefully")
        sys.exit(1)


@click.command()
@click.argument('logins')
@click.argument('repositories', nargs=-1)
def comparison(logins, repositories):
    """Get statistics of several user for specific repositories."""
    # The logins are comma seperated ('test1,test2,rofl,wtf,omfg')
    try:
        plot_comparison(logins, repositories)
    except KeyboardInterrupt:
        logger.info("CTRL-C Exiting Gracefully")
        sys.exit(1)


plot.add_command(comparison)
