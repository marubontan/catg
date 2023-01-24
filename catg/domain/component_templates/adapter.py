from typing import TypedDict
from ..dto.{{use_case}} import {{parsed_object}}OutputDto

class {{parsed_object}}Body(TypedDict):
    pass

class {{parsed_object}}Adapter:
    @classmethod
    def {{use_case}}_output_dto_to_parsed_body({{use_case}}_output_dto: {{parsed_object}}OutputDto) -> {{parsed_object}}Body:
        pass