class Mediator:
    def notify(self, sender, event):
        raise NotImplementedError


class Component:
    def __init__(self, mediator):
        self.mediator = mediator


class Button(Component):
    def click(self):
        self.mediator.notify(self, 'click')


class Console(Component):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.content = ''

    def show(self):
        self.mediator.screen = self.content


class Dialog(Mediator):
    def __init__(self):
        self.screen = ''
        self.button = Button(self)
        self.console = Console(self)

    def notify(self, sender, event):
        if isinstance(sender, Button):
            if event == 'click':
                self.console.content = "Button Clicked."
                self.console.show()
