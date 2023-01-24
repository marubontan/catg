from typing import TypedDict
from ..dto.{{use_case}} import {{dto_class}}

class {{parsed_object}}Body(TypedDict):
    pass

class {{parsed_object}}Adapter:
    @classmethod
    def {{dto_snake}}_to_parsed_body({{dto_snake}}: {{dto_class}}) -> {{parsed_object}}Body:
        pass