import click
import os
from ..domain.use_case.generate_template import GenerateTemplate
from ..domain.use_case.add_use_case import AddUseCase

TEMPLATE_PATTERN_NAME = "template_1"


@click.group()
def cli():
    pass


@cli.command("generate_template")
@click.argument("space_name")
def generate_template(space_name):
    use_case = GenerateTemplate()
    objective_dir = os.path.join(os.getcwd(), space_name)
    use_case.execute(TEMPLATE_PATTERN_NAME, objective_dir)


@cli.command("add_use_case")
@click.argument("use_case_name")
def add_use_case(use_case_name):
    use_case = AddUseCase()
    use_case.execute(use_case_name, os.getcwd())
