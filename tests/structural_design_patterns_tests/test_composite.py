import unittest
from structural_design_patterns.composite import Product, Box


class TestComposite(unittest.TestCase):
    def test(self):
        hammer = Product(100)
        box_a = Box()
        box_a.add(hammer)

        iphone = Product(10000)
        charge_line = Product(10)
        box_b = Box()
        box_b.add(iphone)
        box_b.add(charge_line)

        chargeer = Product(20)
        box_c = Box()
        box_c.add(chargeer)

        box_bigger = Box()
        box_bigger.add(box_b)
        box_bigger.add(box_c)

        box_biggest = Box()
        box_biggest.add(box_bigger)
        box_biggest.add(box_a)

        total_price = box_biggest.get_price()
        self.assertEqual(total_price, 10130)
