import unittest
from .chain_of_responsibility import AdultChecker, ManChecker, Human


class TestBridge(unittest.TestCase):
    def setUp(self):
        self.adult_checker = AdultChecker()
        man_checker = ManChecker()

        self.adult_checker.set_next(man_checker)

    def test_man_adult(self):
        human = Human(18, 'Man')
        is_pass = self.adult_checker.handle(human)

        self.assertEqual(is_pass, True)

    def test_man_not_adult(self):
        human = Human(17, 'Man')
        is_pass = self.adult_checker.handle(human)

        self.assertEqual(is_pass, False)

    def test_woman_adult(self):
        human = Human(18, 'Woman')
        is_pass = self.adult_checker.handle(human)

        self.assertEqual(is_pass, False)

    def test_woman_not_adult(self):
        human = Human(17, 'Woman')
        is_pass = self.adult_checker.handle(human)

        self.assertEqual(is_pass, False)
