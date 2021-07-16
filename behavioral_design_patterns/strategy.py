class Strategy:
    def execute(self, a, b):
        raise NotImplementedError


class ConcreteStrategyAdd(Strategy):
    def execute(self, a, b):
        return a + b


class ConcreteStrategySubtract(Strategy):
    def execute(self, a, b):
        return a - b


class ConcreteStrategyMultiply(Strategy):
    def execute(self, a, b):
        return a * b


class Context:
    strategy = None

    def set_strategy(self, strategy: Strategy):
        self.strategy = strategy

    def executeStrategy(self, a, b):
        return self.strategy.execute(a, b)


class ExampleApplication:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def main(self, action):
        context = Context()

        if (action == 'addition'):
            context.set_strategy(ConcreteStrategyAdd())
        elif (action == 'subtraction'):
            context.set_strategy(ConcreteStrategySubtract())
        elif(action == 'multiplication'):
            context.set_strategy(ConcreteStrategyMultiply())
        else:
            raise Exception(f'action: {action} not support.')

        result = context.executeStrategy(self.a, self.b)

        return result
