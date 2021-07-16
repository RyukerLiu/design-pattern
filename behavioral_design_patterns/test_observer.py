import unittest
from .observer import ScreenListener, LoggingListener, Editor


class TestObserver(unittest.TestCase):
    def test(self):
        editor = Editor()

        screen_listener = ScreenListener()
        log_listener = LoggingListener()

        editor.event_manager.subscribe('open', screen_listener)
        editor.event_manager.subscribe('open', log_listener)
        editor.open_file('Test')
        self.assertEqual(screen_listener.screen, 'Test')
        self.assertEqual(log_listener.log, 'Test')

        editor.event_manager.subscribe('save', log_listener)
        editor.save_file('Test2')
        self.assertEqual(screen_listener.screen, 'Test')
        self.assertEqual(log_listener.log, 'Test2')

        editor.event_manager.unsubscribe('save', log_listener)
        editor.save_file('Test3')
        self.assertEqual(screen_listener.screen, 'Test')
        self.assertEqual(log_listener.log, 'Test2')
