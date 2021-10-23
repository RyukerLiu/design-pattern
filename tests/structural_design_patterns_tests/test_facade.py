import unittest
from structural_design_patterns.facade import MathFacade


class TestFacade(unittest.TestCase):
    def test_sin(self):
        self.assertEqual(MathFacade.sin(1), 0.8414709848078965)

    def test_two_sin_cos(self):
        self.assertEqual(MathFacade.two_sin_cos(1), 0.9092974268256818)
