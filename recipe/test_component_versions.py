#!/usr/bin/env python3

import configparser
import importlib
import sys

import pytest

# list of (package, version) combinations where the git tag isn't just v<version>
CUSTOM_TAGS = {
    ("lalpulsar", "7.0.0"): "lalpulsar-v7.0.0a",
}


def read_versions_setup_cfg(path):
    cp = configparser.ConfigParser()
    with open(path, "r") as file:
        cp.read_file(file)
    return cp['versions']


LALSUITE_COMPONENTS = read_versions_setup_cfg("setup.cfg")


@pytest.mark.parametrize(("package", "version"), LALSUITE_COMPONENTS.items())
def test_version(package, version):
    expected = CUSTOM_TAGS.get(
        (package, version),
        f"{package}-v{version}",
    )
    mod = importlib.import_module(f"{package}.git_version")
    assert mod.tag == expected


if __name__ == "__main__":
    sys.exit(pytest.main(["-v"]))
