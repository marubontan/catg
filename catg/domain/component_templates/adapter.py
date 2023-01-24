from typing import TypedDict
from ..dto.{{use_case}} import {{dto_class}}

class {{parsed_object}}Body(TypedDict):
    pass

# Change the class name
class Adapter:
    @classmethod
    def {{dto_snake}}_to_parsed_body({{dto_class}}) -> {{parsed_object}}Body:
        pass