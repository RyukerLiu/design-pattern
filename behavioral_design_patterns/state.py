class Context:
    def __init__(self, state):
        self.state = state
        self.state.set_context(self)

    def change_state(self, state):
        self.state = state


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
        state = OffState()
        state.set_context(self.context)
        self.context.change_state(state)


class OffState(State):
    def push_power_button(self):
        self.context.is_power_on = True
        state = OnState()
        state.set_context(self.context)
        self.context.change_state(state)
