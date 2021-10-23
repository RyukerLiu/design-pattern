import unittest
from structural_design_patterns.decorator import DoubleCalculator, BaseDecorator, PutResultInDict, PutResultInList


class TestComposite(unittest.TestCase):
    def test_double(self):
        c = DoubleCalculator(10)
        result = c.execute()
        self.assertEqual(result, 20)

    def test_base_decorator(self):
        c = DoubleCalculator(10)
        c = BaseDecorator(c)
        result = c.execute()
        self.assertEqual(result, 20)

    def test_put_result_in_dict_decorator(self):
        c = DoubleCalculator(10)
        c = PutResultInDict(c)
        result = c.execute()
        self.assertEqual(result, {'result': 20})

    def test_put_result_in_list_decorator(self):
        c = DoubleCalculator(10)
        c = PutResultInList(c)
        result = c.execute()
        self.assertEqual(result, [20])

    def test_combination(self):
        c = DoubleCalculator(10)
        c = PutResultInList(c)
        c = PutResultInDict(c)
        result = c.execute()
        self.assertEqual(result, {'result': [20]})
