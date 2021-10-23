import unittest
from behavioral_design_patterns.memento import Screen, Caretaker


class TestMemento(unittest.TestCase):
    def test(self):
        screen = Screen('Hello')
        memento = screen.create_memento()

        caretaker = Caretaker()
        caretaker.history.append(memento)

        screen.set_display_content('New Content')
        self.assertEqual(screen.display_content, 'New Content')

        caretaker.undo()
        self.assertEqual(screen.display_content, 'Hello')

        caretaker.undo()
        self.assertEqual(screen.display_content, 'Hello')
