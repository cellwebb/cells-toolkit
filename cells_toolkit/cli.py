import click
from cells_toolkit.auto_commit import main as auto_commit_main
from cells_toolkit.auto_changelog import main as auto_changelog_main


@click.group()
def cli():
    """Cell's Toolkit CLI"""
    pass


@cli.command()
def gac():
    """Run auto-commit."""
    auto_commit_main()


@cli.command()
def ach():
    """Run auto-changelog."""
    auto_changelog_main()


if __name__ == "__main__":
    cli()
