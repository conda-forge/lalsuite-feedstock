#!/bin/bash

# render the pyproject.toml file
${PYTHON} ${RECIPE_DIR}/render.py

# print rendered pyproject.toml file
echo "Rendered pyproject.toml file:"
echo "===================="
cat pyproject.toml
echo "===================="

# create a wheel using poetry
mkdir -p ${PKG_NAME}
${PYTHON} -m poetry config settings.virtualenvs.path $(pwd)
${PYTHON} -m poetry build --no-interaction --format wheel -vvv

# install the new wheel using pip
${PYTHON} -m pip install dist/${PKG_NAME}-${PKG_VERSION}-*.whl -vvv
