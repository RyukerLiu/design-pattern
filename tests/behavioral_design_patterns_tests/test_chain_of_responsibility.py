import unittest
from behavioral_design_patterns.chain_of_responsibility import (
    AdultChecker,
    ManChecker,
    Human,
    EducationChecker,
)


class TestChainOfResponsibility(unittest.TestCase):
    def setUp(self):
        self.adult_checker = AdultChecker()
        man_checker = ManChecker()
        education_checker = EducationChecker()

        self.adult_checker.set_next(man_checker)
        man_checker.set_next(education_checker)

    def test_all_pass(self):
        human = Human(25, "Man", "bachelor")
        is_pass = self.adult_checker.handle(human)
        self.assertEqual(is_pass, True)

    def test_fail_at_first(self):
        human = Human(17, "Man", "bachelor")
        is_pass = self.adult_checker.handle(human)
        self.assertEqual(is_pass, False)

    def test_fail_at_second(self):
        human = Human(25, "Woman", "bachelor")
        is_pass = self.adult_checker.handle(human)
        self.assertEqual(is_pass, False)

    def test_fail_at_third(self):
        human = Human(25, "Man", "high_school")
        is_pass = self.adult_checker.handle(human)
        self.assertEqual(is_pass, False)
