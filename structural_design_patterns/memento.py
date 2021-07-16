class Originator:
    class Memento:
        def restore(self):
            raise NotImplementedError

    def create_memento(self):
        raise NotImplementedError


class Screen(Originator):
    class ScreenMemento(Originator.Memento):
        def __init__(self, originator, display_content):
            self.originator = originator
            self.display_content = display_content

        def restore(self):
            self.originator.set_display_content(self.display_content)

    def __init__(self, display_content):
        self.display_content = display_content

    def set_display_content(self, display_content):
        self.display_content = display_content

    def create_memento(self):
        memento = Screen.ScreenMemento(self, self.display_content)
        return memento


class Caretaker:
    def __init__(self):
        self.history = []

    def undo(self):
        try:
            memento = self.history.pop(-1)
            memento.restore()
        except IndexError:
            pass
