#!/bin/bash

OUTPUT_DIR="."
CONFIG_FILE="openapi/openapi-config.yaml"
OPENAPI_SPEC="openapi/fitbit-web-api-openapi-fixed.json"
PACKAGE_URL="https://github.com/allenporter/fitbit-web-api"

# Preserve the package version from `pyproject.toml`
CURRENT_VERSION=$(grep -m 1 "version" pyproject.toml | sed -n 's/.*version *= *"\([^"]*\)".*/\1/p')

docker run --rm -v "${PWD}:/data" openapitools/openapi-generator-cli generate \
   --input-spec /data/${OPENAPI_SPEC} \
   --generator-name python \
   --output /data/${OUTPUT_DIR} \
   --config /data/${CONFIG_FILE} \
   --package-name fitbit_web_api \
   --package-version "${CURRENT_VERSION}"

# The generate code changes `pyproject.yaml` in a way that is not
# compatible with the existing project setup. Additionally it changes
# ruff formatting rules. We need to revert these changes to make
# the generated code compatible with the existing project setup.
echo "---"
echo "Reverting changes to python project setup"
rm setup.cfg
git checkout -- pyproject.toml test-requirements.txt

echo "---"
echo "Running ruff to fix code style..."
ruff check --fix .

echo "---"
echo "Running black to format code..."
black .
