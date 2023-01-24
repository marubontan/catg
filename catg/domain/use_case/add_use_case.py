import os
from typing import Dict
from jinja2 import Template
from ...setting import ADAPTER_TEMPLATE, USE_CASE_TEMPLATE, DTO_TEMPLATE


class AddUseCase:
    def __init__(self):
        pass

    def execute(self, use_case_name: str, objective_path: str):
        filling_values = self._compose_filling_values(use_case_name)
        file_name = self._compose_file_name(use_case_name)

        rendered_adapter = self._compose_rendered_content(
            ADAPTER_TEMPLATE, filling_values
        )
        rendered_use_case = self._compose_rendered_content(
            USE_CASE_TEMPLATE, filling_values
        )
        rendered_dto = self._compose_rendered_content(DTO_TEMPLATE, filling_values)

        adapter_file_path = self._compose_file_path(
            objective_path, "adapter", file_name
        )
        use_case_file_path = self._compose_file_path(
            objective_path, "use_case", file_name
        )
        dto_file_path = self._compose_file_path(objective_path, "dto", file_name)

        self._save(rendered_adapter, adapter_file_path)
        self._save(rendered_use_case, use_case_file_path)
        self._save(rendered_dto, dto_file_path)

    @staticmethod
    def _compose_file_path(base_path: str, target: str, file_name: str) -> str:
        return os.path.join(base_path, target, file_name)

    def _compose_filling_values(self, use_case_name: str) -> Dict:
        dto_class = self._compose_dto_class_name(use_case_name)
        dto_snake = self._compose_dto_snake_name(use_case_name)
        parsed_object = self._compose_parsed_object_name(use_case_name)
        return {
            "use_case": use_case_name,
            "dto_class": dto_class,
            "dto_snake": dto_snake,
            "parsed_object": parsed_object,
        }

    def _compose_rendered_content(self, file_path: str, filling_values: Dict) -> str:
        template = self._load_template(file_path)
        return template.render(filling_values)

    @staticmethod
    def _render_template(template: Template, filling_values: Dict) -> str:
        return template.render(filling_values)

    @staticmethod
    def _compose_file_name(user_case_name: str) -> str:
        return f"{user_case_name}.py"

    @staticmethod
    def _compose_parsed_object_name(use_case_name: str) -> str:
        return "".join([word.capitalize() for word in f"{use_case_name}".split("_")])

    @staticmethod
    def _compose_dto_snake_name(use_case_name: str) -> str:
        return f"{use_case_name}_dto"

    @staticmethod
    def _compose_dto_class_name(use_case_name: str) -> str:
        return "".join(
            [word.capitalize() for word in f"{use_case_name}_dto".split("_")]
        )

    @staticmethod
    def _load_template(file_path: str) -> Template:
        with open(file_path) as f:
            template = Template(f.read())
        return template

    @staticmethod
    def _save(content: str, file_path: str):
        with open(file_path, "w") as f:
            f.write(content)
