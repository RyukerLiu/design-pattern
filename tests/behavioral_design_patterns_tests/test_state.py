import unittest
from .state import Tv, OffState, OnState


class TestState(unittest.TestCase):
    def test(self):

        off = OffState()
        tv = Tv(off)

        tv.push_power_button()
        self.assertEqual(tv.is_power_on, True)
        self.assertEqual(type(tv.state), OnState)

        tv.push_power_button()
        self.assertEqual(tv.is_power_on, False)
        self.assertEqual(type(tv.state), OffState)
