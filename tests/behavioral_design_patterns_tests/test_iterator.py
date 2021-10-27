import unittest
from behavioral_design_patterns.iterator import List


class TestIterator(unittest.TestCase):
    def setUp(self) -> None:
        self.list = List([1, 2, 3])

    def test_list_forward_iterator(self):
        iter = self.list.get_forward_iterator()

        elements = []
        while iter.has_more():
            elements.append(iter.get_next())

        self.assertEqual(elements, [1, 2, 3])

    def test_list_backward_iterator(self):
        iter = self.list.get_backward_iterator()

        elements = []
        while iter.has_more():
            elements.append(iter.get_next())

        self.assertEqual(elements, [3, 2, 1])

    def test_list_pythonic_iterator(self):
        elements = [ element for element in self.list]

        self.assertEqual(elements, [1, 2, 3])