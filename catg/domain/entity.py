import os
from dataclasses import dataclass, field
from ..setting import TEMPLATE_DIR_PATH


@dataclass
class Template:
    name: str
    path: float = field(init=False)

    def __post_init__(self):
        self.path = os.path.join(TEMPLATE_DIR_PATH, self.name)
