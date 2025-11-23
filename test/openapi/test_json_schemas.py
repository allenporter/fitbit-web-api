import json
import pathlib

import pytest

# Define the path to the schemas directory
PROJECT_ROOT = pathlib.Path(__file__).parent.parent.parent
SCHEMA_DIR = PROJECT_ROOT / "openapi" / "model"


def get_schema_files():
    """Yields all JSON files in the schema directory."""
    for schema_file in SCHEMA_DIR.rglob("*.json"):
        yield schema_file


@pytest.mark.parametrize("schema_file", get_schema_files(), ids=lambda p: p.name)
def test_schema_is_valid_json(schema_file):
    """Verifies that the schema file contains valid JSON."""
    content = schema_file.read_text()
    try:
        json.loads(content)
    except json.JSONDecodeError as e:
        pytest.fail(f"Invalid JSON in {schema_file}: {e}")
