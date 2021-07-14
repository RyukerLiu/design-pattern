class Component:
    def execute(self):
        raise NotImplementedError


class DoubleCalculator(Component):
    def __init__(self, value):
        self.value = value

    def execute(self):
        return self.value * 2


class BaseDecorator(Component):
    def __init__(self, component):
        self.wrappee = component

    def execute(self):
        return self.wrappee.execute()


class PutResultInList(BaseDecorator):
    def __init__(self, component):
        self.wrappee = component

    def execute(self):
        return [self.wrappee.execute()]


class PutResultInDict(BaseDecorator):
    def __init__(self, component):
        self.wrappee = component

    def execute(self):
        return {'result': self.wrappee.execute()}
