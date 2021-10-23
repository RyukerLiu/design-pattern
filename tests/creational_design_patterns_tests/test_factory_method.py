import unittest
from .factory_method import Application


class TestApplication(unittest.TestCase):
    def test_windows_button_render(self):
        app = Application('Windows')

        self.assertEqual(app.dialog.content, 'Windows Button')

    def test_html_button_render(self):
        app = Application('Web')

        self.assertEqual(app.dialog.content, 'Html Button')

    def test_windows_button_click(self):
        app = Application('Windows')
        app.click_button()

        self.assertEqual(app.message, 'Windows Button On Click')

    def test_html_button_click(self):
        app = Application('Web')
        app.click_button()

        self.assertEqual(app.message, 'Html Button On Click')
