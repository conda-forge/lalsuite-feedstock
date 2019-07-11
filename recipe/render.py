#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from os.path import join

import jinja2

import yaml

RECIPE_DIR = os.environ["RECIPE_DIR"]


def parse_meta_yaml(filename):
    """Parse a conda build meta.yaml file, including jinja2 variables
    """
    with open(filename, "r") as fobj:
        raw = fobj.read()
    return yaml.load(jinja2.Template(raw).render(), Loader=yaml.Loader)


# parse the meta.yaml file, and get the basic info
meta = parse_meta_yaml(join(RECIPE_DIR, "meta.yaml"))

# write a formatted pyproject.toml file for poetry to use
with open(join(RECIPE_DIR, "pyproject.toml.in"), "r") as fobj:
    with open("pyproject.toml", "w") as fout:
        fout.write(jinja2.Template(fobj.read()).render(meta=meta))
