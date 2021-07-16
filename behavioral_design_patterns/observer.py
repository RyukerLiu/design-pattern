from collections import defaultdict


class EventManager:
    def __init__(self):
        self.event_listeners = defaultdict(list)

    def subscribe(self, event_type, listener):
        self.event_listeners[event_type].append(listener)

    def unsubscribe(self, event_type, listener):
        self.event_listeners[event_type].remove(listener)

    def notify(self, event_type, data):
        for listener in self.event_listeners[event_type]:
            listener.update(data)


class Editor:
    def __init__(self):
        self.event_manager = EventManager()

    def open_file(self, filename):
        self.event_manager.notify("open", filename)

    def save_file(self, filename):
        self.event_manager.notify("save", filename)


class EventListener:
    def update(self, filename):
        raise NotImplementedError


class LoggingListener(EventListener):
    def __init__(self):
        self.log = ''

    def update(self, filename):
        self.log = filename


class ScreenListener(EventListener):
    def __init__(self):
        self.screen = ''

    def update(self, filename):
        self.screen = filename
