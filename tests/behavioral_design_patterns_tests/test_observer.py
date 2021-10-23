import unittest
from behavioral_design_patterns.observer import Editor, ScreenListener, LoggingListener


class TestObserver(unittest.TestCase):
    def test(self):
        editor = Editor()

        screen_listener = ScreenListener(editor.event_manager)
        log_listener = LoggingListener(editor.event_manager)

        editor.open_file('Test')
        self.assertEqual(screen_listener.screen, 'open Test')
        self.assertEqual(log_listener.log, 'open Test')

        editor.save_file('Test2')
        self.assertEqual(screen_listener.screen, 'save Test2')
        self.assertEqual(log_listener.log, 'save Test2')
