class Prototype:
    def clone(self):
        raise NotImplementedError


class Person(Prototype):
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def clone(self):
        return Person(self.name + '_Cloned', self.age, self.weight)

    def __copy__(self):
        return self.clone()
