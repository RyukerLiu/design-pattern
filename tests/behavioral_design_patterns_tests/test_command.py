import unittest
from behavioral_design_patterns.command import EditorApplication


class TestEditorApplication(unittest.TestCase):
    def setUp(self):
        self.app = EditorApplication()
        self.assertEqual(self.app.clipboard, '')

    def test_copy(self):
        self.app.editor.text = 'Test'
        self.app.editor.select('Test')
        self.app.copy_button.push()

        self.assertEqual(self.app.clipboard, 'Test')
        self.assertEqual(self.app.editor.text, 'Test')

    def test_paste(self):
        self.app.clipboard = 'Test'
        self.app.paste_button.push()

        self.assertEqual(self.app.editor.text, 'Test')

    def test_cut(self):
        self.app.editor.text = 'Test'
        self.app.editor.select('Test')
        self.app.cut_button.push()

        self.assertEqual(self.app.clipboard, 'Test')
        self.assertEqual(self.app.editor.text, '')

    def test_undo_paste(self):
        self.app.clipboard = 'Test'
        self.app.paste_button.push()
        self.assertEqual(self.app.editor.text, 'Test')

        self.app.undo_button.push()
        self.assertEqual(self.app.editor.text, '')

    def test_undo_cut(self):
        self.app.editor.text = 'Test'
        self.app.editor.select('Test')
        self.app.cut_button.push()

        self.assertEqual(self.app.clipboard, 'Test')
        self.assertEqual(self.app.editor.text, '')

        self.app.undo_button.push()
        self.assertEqual(self.app.editor.text, 'Test')

    def test_undo_undo(self):
        self.app.clipboard = 'Test'
        self.app.paste_button.push()
        self.assertEqual(self.app.editor.text, 'Test')

        self.app.undo_button.push()
        self.assertEqual(self.app.editor.text, '')

        self.app.undo_button.push()
        self.assertEqual(self.app.editor.text, 'Test')
