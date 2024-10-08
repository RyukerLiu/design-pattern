class QualificationChecker:
    next = None

    def set_next(self, handler):
        self.next = handler

    def handle(self, human) -> bool:
        """
        If pass, call next
        """
        is_pass = self.check(human)

        if is_pass:
            if self.next:
                return self.next.handle(human)
            else:
                return True
        else:
            return False

    def check(self, human):
        raise NotImplementedError


class AdultChecker(QualificationChecker):
    def check(self, human):
        if human.age >= 18:
            return True
        else:
            return False


class ManChecker(QualificationChecker):
    def check(self, human):
        if human.sex == "Man":
            return True
        else:
            return False


EDUCATION_ORDER = ["high_school", "bachelor", "master", "phd"]


class EducationChecker(QualificationChecker):
    def check(self, human):
        return EDUCATION_ORDER.index(human.education_level) >= EDUCATION_ORDER.index(
            "bachelor"
        )


class Human:
    def __init__(self, age, sex, education_level):
        self.age = age
        self.sex = sex
        self.education_level = education_level
