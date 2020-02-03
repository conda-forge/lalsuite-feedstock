#!/bin/bash

# copy over the pyproject.toml
cp -v ${RECIPE_DIR}/pyproject.toml .

echo "pyproject.toml file:"
echo "===================="
cat pyproject.toml
echo "===================="

# render the setup.cfg file
${PYTHON} ${RECIPE_DIR}/render.py

# print rendered setup.cfg file
echo "Rendered setup.cfg file:"
echo "===================="
cat setup.cfg
echo "===================="

# install the new package
${PYTHON} -m pip install .
