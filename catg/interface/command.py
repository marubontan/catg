import click
import os
from ..domain.use_case.generate_template import GenerateTemplate
from ..setting import VALID_TEMPLATES


def validate_template(ctx, param, value):
    if value not in VALID_TEMPLATES:
        print(value)
        raise click.BadParameter(f"Allowed templates are {VALID_TEMPLATES}")
    return value


@click.group()
def cli():
    pass


@cli.command("generate_template")
@click.argument("template_pattern_name", callback=validate_template)
def generate_template(template_pattern_name):
    use_case = GenerateTemplate()
    objective_dir = os.path.join(os.getcwd(), template_pattern_name)
    use_case.execute(template_pattern_name, objective_dir)
