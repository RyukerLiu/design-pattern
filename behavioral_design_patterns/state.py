class Context:
    def __init__(self, state):
        self.change_state(state)

    def change_state(self, state):
        self.state = state
        self.state.set_context(self)


class Tv(Context):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_power_on = False

    def push_power_button(self):
        self.state.push_power_button()


class State:
    def set_context(self, context):
        self.context = context

    def push_power_button(self):
        NotImplementedError


class OnState(State):
    def push_power_button(self):
        self.context.is_power_on = False
        self.context.change_state(OffState())


class OffState(State):
    def push_power_button(self):
        self.context.is_power_on = True
        self.context.change_state(OnState())
