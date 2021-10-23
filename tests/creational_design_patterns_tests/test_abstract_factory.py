import unittest
from creational_design_patterns.abstract_factory_main import get_furniture


class TestAbstractFactoryMain(unittest.TestCase):
    def test_get_victorian_furniture(self):
        chair, coffee_table, sofa = get_furniture('Victorian')
        self.assertEqual(str(chair), 'VictorianChair')
        self.assertEqual(str(coffee_table), 'VictorianCoffeTable')
        self.assertEqual(str(sofa), 'VictorianSofa')

    def test_get_modern_furniture(self):
        chair, coffee_table, sofa = get_furniture('Modern')
        self.assertEqual('foo'.upper(), 'FOO')
        self.assertEqual(str(chair), 'ModernChair')
        self.assertEqual(str(coffee_table), 'ModernCoffeTable')
        self.assertEqual(str(sofa), 'ModernSofa')
