class EditorCommand:
    app = None
    editor = None
    backup = None

    def __init__(self, app):
        self.app = app
        self.editor = self.app.editor

    def save_backup(self):
        self.backup = self.editor.text

    def undo(self):
        self.editor.text = self.backup

    def execute(self):
        raise NotImplementedError


class CopyCommand(EditorCommand):
    def execute(self):
        self.save_backup()
        self.app.clipboard = self.editor.get_selection()


class CutCommand(EditorCommand):
    def execute(self):
        self.save_backup()
        self.app.clipboard = self.editor.get_selection()
        self.editor.delete_selection()


class PasteCommand(EditorCommand):
    def execute(self):
        self.save_backup()
        self.editor.replace_selection(self.app.clipboard)


class UndoCommand(EditorCommand):
    def execute(self):
        self.save_backup()
        self.app.undo()


class Editor:
    def __init__(self, text):
        self.text = text
        self.selection = ''

    def get_selection(self):
        return self.selection

    def delete_selection(self):
        self.text = self.text.replace(self.selection, '')

    def replace_selection(self, replace_text):
        self.delete_selection()
        self.text += replace_text

    def select(self, select_text):
        self.selection = select_text


class Button:
    def set_function(self, function):
        self.function = function

    def push(self):
        self.function()


class EditorApplication:
    def __init__(self):
        self.clipboard = ''
        self.editor = Editor('')
        self.command_history = []

        self.__create_ui()

    def __create_ui(self):
        def copy():
            self.execute_command(CopyCommand(self))
        self.copy_button = Button()
        self.copy_button.set_function(copy)

        def cut():
            self.execute_command(CutCommand(self))
        self.cut_button = Button()
        self.cut_button.set_function(cut)

        def paste():
            self.execute_command(PasteCommand(self))
        self.paste_button = Button()
        self.paste_button.set_function(paste)

        def undo():
            self.execute_command(UndoCommand(self))
        self.undo_button = Button()
        self.undo_button.set_function(undo)

    def execute_command(self, command):
        command.execute()
        self.command_history.append(command)

    def undo(self):
        command = self.command_history.pop()
        if command is not None:
            command.undo()
