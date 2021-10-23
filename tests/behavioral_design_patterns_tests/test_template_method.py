import unittest
from .template_method import HolyStringGenerator, DarkStringGenerator, StringGenerator


class TestTemplateMethod(unittest.TestCase):
    def test(self):
        g = StringGenerator()
        string = g.get_string()
        self.assertEqual(string, 'firstsecondthird')

    def test(self):
        g = HolyStringGenerator()
        string = g.get_string()
        self.assertEqual(string, 'firstholythird')

    def test(self):
        g = DarkStringGenerator()
        string = g.get_string()
        self.assertEqual(string, 'firstdarkthird')
