import os

TEMPLATE_DIR_PATH = os.path.join(os.path.dirname(__file__), "domain", "templates")

COMPONENT_DIR_PATH = os.path.join(
    os.path.dirname(__file__), "domain", "component_templates"
)
ADAPTER_TEMPLATE = os.path.join(COMPONENT_DIR_PATH, "adapter.py")
DTO_TEMPLATE = os.path.join(COMPONENT_DIR_PATH, "dto.py")
USE_CASE_TEMPLATE = os.path.join(COMPONENT_DIR_PATH, "use_case.py")
