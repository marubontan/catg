from distutils.dir_util import copy_tree
from ..entity import Template


class GenerateTemplate:
    def __init__(self):
        pass

    def execute(self, template_name: str, objective_path: str):
        template = Template(template_name)
        copy_tree(template.path, objective_path)
