from unittest import TestCase

from {{cookiecutter.package_name}}.const import extension


def test_extension_name():
    assert extension.name == "{{ cookiecutter.package_name }}"
