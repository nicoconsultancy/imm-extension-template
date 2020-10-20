from unittest import TestCase

from {{ cookiecutter.package_name }}.const import extension

class TestExtension(TestCase):
  def setUp(self):
    pass

  def test_extension(self):
    self.assertTrue(extension)