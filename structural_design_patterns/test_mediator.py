import unittest
from .mediator import Dialog


class TestMediator(unittest.TestCase):
    def test(self):
        dialog = Dialog()
        dialog.button.click()

        self.assertEqual(dialog.screen, 'Button Clicked.')
