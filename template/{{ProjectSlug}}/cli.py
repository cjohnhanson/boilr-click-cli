import click

@click.group()
def cli():
    """
    {{Description}}
    """
    pass

@cli.command()
def version():
    """
    Print the version and exit
    """
    click.echo("{{Version}}")
