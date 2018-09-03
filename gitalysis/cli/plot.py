from gitalizer.plot import (
    plot_user as plot_user_func,
    plot_employee,
    plot_comparison as plot_comparison_func,
)

from gitalizer.analysis import (
    analyse_travel_path,
    analyse_punch_card,
)
# ----- Plotting / Data mining -----

@app.cli.command()
@click.argument('login')
def plot_user(login):
    """Plot all graphs for a specific github user."""
    try:
        plot_user_func(login)
    except KeyboardInterrupt:
        app.logger.info("CTRL-C Exiting Gracefully")
        sys.exit(1)

@app.cli.command()
@click.argument('login')
@click.argument('repositories', nargs=-1)
def plot_user_for_repositories(login, repositories):
    """Get statistics of an user for specific repositories."""
    try:
        plot_employee(login, repositories)
    except KeyboardInterrupt:
        app.logger.info("CTRL-C Exiting Gracefully")
        sys.exit(1)

@app.cli.command()
@click.argument('logins')
@click.argument('repositories', nargs=-1)
def plot_comparison(logins, repositories):
    """Get statistics of several user for specific repositories."""
    # The logins are comma seperated ('test1,test2,rofl,wtf,omfg')
    try:
        plot_comparison_func(logins, repositories)
    except KeyboardInterrupt:
        app.logger.info("CTRL-C Exiting Gracefully")
        sys.exit(1)

# ----- Analysis -------
@app.cli.command()
@click.option('--existing/-e', default=False)
def analyse_travel(existing):
    """Analyse missing time stuff."""
    try:
        analyse_travel_path(existing)
    except KeyboardInterrupt:
        app.logger.info("CTRL-C Exiting Gracefully")
        sys.exit(1)

@app.cli.command()
@click.option('--existing/-e', default=False)
def analyse_punch(existing):
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
        app.logger.info("CTRL-C Exiting Gracefully")
        sys.exit(1)

