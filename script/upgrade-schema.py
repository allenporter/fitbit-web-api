#!env python3
#
# This script updates the Fitweb Web API schema with things that are incorrect
# or missing.

import json
import pathlib
from typing import Any

OPENAPI_DIR = pathlib.Path("openapi")
OPENAPI_SCHEMA = OPENAPI_DIR / "fitbit-web-api-openapi.json"
FIXED_SCHEMA = OPENAPI_DIR / "fitbit-web-api-openapi-fixed.json"

MODEL_DIR = OPENAPI_DIR / "model"
PATHS_DIR = OPENAPI_DIR / "paths"

MEAL_ID_PARAM = {
    "name": "meal-id",
    "in": "path",
    "required": True,
    "description": "The ID of the meal.",
    "schema": {
        "type": "string",
    },
}


def snake_to_pascal(name: str) -> str:
    """Converts a snake_case string to PascalCase."""
    return "".join(word.capitalize() for word in name.split("_"))


def load_path_config() -> dict[str, Any]:
    """Load path configurations from the openapi/paths directory."""
    path_config = {}
    for path_file in PATHS_DIR.glob("*.json"):
        with path_file.open("r") as f:
            path_config.update(json.load(f))
    return path_config


def fix_schema_bugs(schema: dict[str, Any]) -> None:
    """Fix known bugs in the OpenAPI schema."""
    # This path is defined twice, once with a meal-id and once without.
    # The one without is not in the documentation, so we remove it.
    del schema["paths"]["/1/user/-/meals.json"]
    # This path is missing the meal-id parameter.
    post_op = schema["paths"]["/1/user/-/meals/{meal-id}.json"]["post"]
    if "parameters" not in post_op:
        post_op["parameters"] = []
    post_op["parameters"].append(MEAL_ID_PARAM)
    # This path is missing the post operation, and there is a stray 'post' key
    if "post" in schema["paths"]:
        schema["paths"]["/1/user/-/profile.json"]["post"] = schema["paths"]["post"]
        del schema["paths"]["post"]
    # The post operation is missing a responses object
    if "responses" not in schema["paths"]["/1/user/-/profile.json"]["post"]:
        schema["paths"]["/1/user/-/profile.json"]["post"]["responses"] = {}


def update_schemas(schema: dict[str, Any]) -> None:
    """Update the OpenAPI schema with response objects."""
    # Load all the model schemas from the openapi/model directory.
    print("Loading component schemas from openapi/model...")
    for model_file in MODEL_DIR.rglob("*.json"):
        with model_file.open("r") as f:
            model_schema = json.load(f)
            schema_name = snake_to_pascal(model_file.stem)
            print(f"  - Loading {model_file.relative_to(MODEL_DIR)} as {schema_name}")
            schema["components"]["schemas"][schema_name] = model_schema

    path_config = load_path_config()
    print("Updating paths with response objects...")
    for path, methods in path_config.items():
        for method, responses in methods.items():
            for status_code, response_name in responses.items():
                if not response_name:
                    continue
                print(f"  - Updating {method.upper()} {path} with {response_name}")
                schema["paths"][path][method]["responses"][status_code] = {
                    "description": "A successful request.",
                    "content": {
                        "application/json": {
                            "schema": {"$ref": f"#/components/schemas/{response_name}"}
                        }
                    },
                }


def generate_fixed_schema() -> dict[str, Any]:
    """Generates the fixed OpenAPI schema."""
    with OPENAPI_SCHEMA.open() as f:
        schema = json.load(f)

    fix_schema_bugs(schema)
    update_schemas(schema)
    return schema


def main() -> None:
    """Load the OpenAPI schema, fix bugs, and write the updated schema."""
    schema = generate_fixed_schema()

    with FIXED_SCHEMA.open("w") as f:
        json.dump(schema, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()
