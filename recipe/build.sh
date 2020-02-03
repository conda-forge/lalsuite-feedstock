#!/bin/bash

# render the setup.cfg file
${PYTHON} ${RECIPE_DIR}/render.py

# print rendered setup.cfg file
echo "Rendered setup.cfg file:"
echo "===================="
cat setup.cfg
echo "===================="

# install the new package
${PYTHON} -m pip install .
