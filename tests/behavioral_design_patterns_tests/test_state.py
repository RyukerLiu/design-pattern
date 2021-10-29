import unittest
from behavioral_design_patterns.state import Tv, OffState, OnState


class TestState(unittest.TestCase):
    def test(self):
        tv = Tv()
        self.assertEqual(type(tv.state), OffState)

        tv.push_power_button()
        self.assertEqual(type(tv.state), OnState)

        tv.push_power_button()
        self.assertEqual(type(tv.state), OffState)
