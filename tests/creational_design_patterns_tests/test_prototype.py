import copy
import unittest

from creational_design_patterns.prototype import Person


class TestPrototype(unittest.TestCase):
    def test(self):
        ted = Person('Ted', 18, 50)
        cloned_ted = ted.clone()

        self.assertIsNot(ted, cloned_ted)
        self.assertEqual(ted.name + '_Cloned', cloned_ted.name)
        self.assertEqual(ted.age, cloned_ted.age)
        self.assertEqual(ted.weight, cloned_ted.weight)

    def test_copy(self):
        ted = Person('Ted', 18, 50)
        coppied_ted = copy.copy(ted)

        self.assertIsNot(ted, coppied_ted)
        self.assertEqual(ted.name + '_Cloned', coppied_ted.name)
        self.assertEqual(ted.age, coppied_ted.age)
        self.assertEqual(ted.weight, coppied_ted.weight)
