import unittest
import observer


class TestObserver(unittest.TestCase):
    def test(self):
        editor = Editor()

        screen_listener = ScreenListener(editor.event_manager)
        log_listener = LoggingListener(editor.event_manager)

        editor.open_file('Test')
        self.assertEqual(screen_listener.screen, 'Test')
        self.assertEqual(log_listener.log, 'Test')

        editor.save_file('Test2')
        self.assertEqual(screen_listener.screen, 'Test')
        self.assertEqual(log_listener.log, 'Test2')
