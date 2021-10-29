class Context:
    def set_state(self, state):
        self.state = state


class Tv(Context):
    def __init__(self):
        self.off_state = OffState(self)
        self.on_state = OnState(self)
        self.state = self.off_state

    def push_power_button(self):
        self.state.push_power_button()


class State:
    def __init__(self, context):
        self.context = context

    def push_power_button(self):
        NotImplementedError


class OnState(State):
    def push_power_button(self):
        self.context.set_state(self.context.off_state)


class OffState(State):
    def push_power_button(self):
        self.context.set_state(self.context.on_state)
