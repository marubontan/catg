from typing import TypedDict
from ..dto.{{use_case}} import {{parsed_object}}InputDto, {{parsed_object}}OutputDto


class {{parsed_object}}RequestBody(TypedDict):
    pass

class {{parsed_object}}ResponseBody(TypedDict):
    pass

class {{parsed_object}}Adapter:
    @classmethod
    def {{use_case}}_request_body_to_input_dto({{use_case}}_request_body: {{parsed_object}}RequestBody) -> {{parsed_object}}InputDto:
        pass

    @classmethod
    def {{use_case}}_output_dto_to_response_body({{use_case}}_output_dto: {{parsed_object}}OutputDto) -> {{parsed_object}}ResponseBody:
        pass