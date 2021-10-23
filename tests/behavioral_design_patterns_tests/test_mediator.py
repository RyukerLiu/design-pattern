import unittest
from behavioral_design_patterns.mediator import Dialog


class TestMediator(unittest.TestCase):
    def test(self):
        dialog = Dialog()
        dialog.button.click()

        self.assertEqual(dialog.screen, 'Button Clicked.')
