import unittest
from .adapter import RoundHole, RoundPeg, SquarePegAdapter, SquarePeg


class TestAdapter(unittest.TestCase):
    def test_fits_with_round_hole_and_round_peg(self):
        round_hole = RoundHole(5)
        round_peg = RoundPeg(5)

        self.assertTrue(round_hole.fits(round_peg))

    def test_fits_with_round_hole_and_square_peg(self):
        round_hole = RoundHole(5)
        square_peg = SquarePeg(5)

        with self.assertRaises(AttributeError) as cm:
            round_hole.fits(square_peg)

        exc = cm.exception
        self.assertEqual(
            str(exc), "'SquarePeg' object has no attribute 'get_radius'")

    def test_fits_with_round_hole_and_square_adapter(self):
        round_hole = RoundHole(5)
        square_peg = SquarePeg(5)
        square_peg_adapter = SquarePegAdapter(square_peg)

        self.assertTrue(round_hole.fits(square_peg_adapter))
