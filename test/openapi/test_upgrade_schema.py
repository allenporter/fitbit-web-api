import json
import pathlib
import sys
from importlib.util import module_from_spec, spec_from_file_location

# Define paths
PROJECT_ROOT = pathlib.Path(__file__).parents[2]
SCRIPT_PATH = PROJECT_ROOT / "script" / "upgrade-schema.py"
FIXED_SCHEMA_PATH = PROJECT_ROOT / "openapi" / "fitbit-web-api-openapi-fixed.json"


def load_upgrade_schema_module():
    """Dynamically loads the upgrade-schema.py module."""
    spec = spec_from_file_location("upgrade_schema", SCRIPT_PATH)
    module = module_from_spec(spec)
    sys.modules["upgrade_schema"] = module
    spec.loader.exec_module(module)
    return module


def test_schema_is_up_to_date():
    """Verifies that the fixed schema on disk matches the generated schema."""
    upgrade_schema = load_upgrade_schema_module()

    # Generate the schema in memory
    generated_schema = upgrade_schema.generate_fixed_schema()

    # Load the schema from disk
    with open(FIXED_SCHEMA_PATH) as f:
        current_schema = json.load(f)

    # Compare the two schemas
    # We compare them as dictionaries to ignore formatting differences
    assert generated_schema == current_schema, (
        "The generated schema does not match the schema on disk. "
        "Please run 'python3 script/upgrade-schema.py' to update the schema."
    )
