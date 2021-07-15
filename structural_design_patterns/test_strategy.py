import unittest
from .strategy import ExampleApplication


class TestStrategy(unittest.TestCase):
    def setUp(self) -> None:
        self.app = ExampleApplication(1, 2)

    def test_add(self):
        result = self.app.main('addition')

        self.assertEqual(result, 3)

    def test_sub(self):
        result = self.app.main('subtraction')

        self.assertEqual(result, -1)

    def test_multiplication(self):
        result = self.app.main('multiplication')

        self.assertEqual(result, 2)
