#!/usr/bin/env python3

import configparser
import importlib
import os
import sys
from pathlib import Path

import pytest


def read_versions_setup_cfg(path):
    cp = configparser.ConfigParser()
    with open(path, "r") as file:
        cp.read_file(file)
    return cp['versions']


LALSUITE_COMPONENTS = read_versions_setup_cfg("setup.cfg")

@pytest.mark.parametrize(("package", "version"), LALSUITE_COMPONENTS.items())
def test_version(package, version):
    mod = importlib.import_module(f"{package}.git_version")
    assert mod.tag == f"{package}-v{version}"


if __name__ == "__main__":
    sys.exit(pytest.main(["-v"]))
