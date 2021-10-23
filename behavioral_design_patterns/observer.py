from collections import defaultdict


class EventManager:
    def __init__(self):
        self.event_listeners = defaultdict(list)

    def subscribe(self, event_type, listener):
        self.event_listeners[event_type].append(listener)

    def unsubscribe(self, event_type, listener):
        self.event_listeners[event_type].remove(listener)

    def notify(self, event_type, filename):
        for listener in self.event_listeners[event_type]:
            listener.update(event_type, filename)


class Editor:
    def __init__(self):
        self.event_manager = EventManager()

    def open_file(self, filename):
        self.event_manager.notify("open", filename)

    def save_file(self, filename):
        self.event_manager.notify("save", filename)


class EventListener:
    def __init__(self, event_manager):
        self.event_manager = event_manager
        event_manager.subscribe('open', self)
        event_manager.subscribe('save', self)

    def update(self, event_type, filename):
        raise NotImplementedError


class LoggingListener(EventListener):
    def __init__(self, event_manager):
        super().__init__(event_manager)
        self.log = ''

    def update(self, event_type, filename):
        self.log = event_type + ' ' + filename


class ScreenListener(EventListener):
    def __init__(self, event_manager):
        super().__init__(event_manager)
        self.screen = ''

    def update(self, event_type, filename):
        self.screen = event_type + ' ' + filename
