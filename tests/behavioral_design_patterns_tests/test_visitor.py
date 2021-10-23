import unittest
from .visitor import Visitor, ElementB, Element, ElementA


class TestVisitor(unittest.TestCase):
    def test(self):
        v = Visitor()

        elements = [Element(), ElementA(), ElementB()]

        results = []
        for element in elements:
            results.append(element.accept(v))

        self.assertEqual(results, ['', 'A', 'B'])
