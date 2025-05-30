import click
from form_filler import fill_form

@click.group()
def cli():
    """AI-Powered Form Filler CLI Tool"""
    pass

@cli.command(name="fill-form")
@click.option('--template', type=click.Path(exists=True), required=True, help='Path to the form template JSON file.')
@click.option('--profile', type=click.Path(exists=True), required=True, help='Path to the user profile PDF/JSON file.')
@click.option('--position', type=str, required=True, help='Position applied.')
@click.option('--jb', type=click.Path(exists=True), required=True, help='Path to the job description txt file.')
@click.option('--output', type=click.Path(), required=True, help='Path to save the filled output file.')
def fill_form_command(template, profile, position, jb, output):
    """Fill a form template using the user profile and Amazon Q."""
    try:
        fill_form(template, profile, position, jb, output)
        click.echo(f"From filled successfully! Save to {output}")
    except Exception as e:
        click.echo(f"Error:{e}")

if __name__=="__main__":
    cli()



