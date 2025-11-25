#!/bin/bash

set -e

OUTPUT_DIR="."
CONFIG_FILE="openapi/openapi-config.yaml"
OPENAPI_SPEC="openapi/fitbit-web-api-openapi-fixed.json"
PACKAGE_URL="https://github.com/allenporter/fitbit-web-api"

# Preserve the package version from `pyproject.toml`
CURRENT_VERSION=$(grep -m 1 "version" pyproject.toml | sed -n 's/.*version *= *"\([^"]*\)".*/\1/p')
OPENAPI_GENERATOR_VERSION=$(cat .openapi-generator/VERSION)

docker run --rm -v "${PWD}:/data" openapitools/openapi-generator-cli:v${OPENAPI_GENERATOR_VERSION} generate \
   --input-spec /data/${OPENAPI_SPEC} \
   --generator-name python \
   --output /data/${OUTPUT_DIR} \
   --config /data/${CONFIG_FILE} \
   --package-name fitbit_web_api

# The flag used to set the version of the generated package
#   --package-version="${CURRENT_VERSION}"
# but that no longer works so for now set it manually
sed -i.bak "s|^__version__ = \".*\"$|__version__ = \"$CURRENT_VERSION\"|" fitbit_web_api/__init__.py
rm fitbit_web_api/__init__.py.bak

# The generate code changes `pyproject.yaml` in a way that is not
# compatible with the existing project setup. Additionally it changes
# ruff formatting rules. We need to revert these changes to make
# the generated code compatible with the existing project setup.
echo "---"
echo "Reverting changes to python project setup"
rm setup.cfg
git checkout -- pyproject.toml test-requirements.txt .gitignore

# Apply patches to fix issues or add features in the generated code
echo "---"
echo "Applying patches to generated code..."
for patch in script/patches/*.patch; do
    echo "Applying patch: $patch"
    patch -p1 < $patch
done
find . -name \*.orig -delete

echo "---"
echo "Running ruff to fix code style..."
ruff check --fix . || true

echo "---"
echo "Running ruff to format code..."
ruff format .

echo "---"
echo "Please stage files and run `pre-commit` to run additional format fixes."
