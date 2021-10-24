class Command:
    def execute(self):
        raise NotImplementedError

    def undo(self):
        raise NotImplementedError

class EditorCommand(Command):
    def __init__(self, editor):
        self.editor = editor
        self.backup = None

    def save_backup(self):
        self.backup = self.editor.text

    def undo(self):
        if self.backup is not None:
            self.editor.text = self.backup

    def execute(self):
        self.save_backup()
        self.action()
    
    def action(self):
        raise NotImplementedError


class CopyCommand(EditorCommand):
    def action(self):
        self.editor.clipboard = self.editor.get_selection()


class CutCommand(EditorCommand):
    def action(self):
        self.editor.clipboard = self.editor.get_selection()
        self.editor.delete_selection()


class PasteCommand(EditorCommand):
    def action(self):
        self.editor.replace_selection(self.editor.clipboard)


class Editor:
    def __init__(self, text):
        self.text = text
        self.clipboard = ''
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
    def __init__(self, function):
        self.function = function

    def push(self):
        self.function()


class EditorApplication:
    def __init__(self):
        self.editor = Editor('')
        self.command_history = []

        self.__create_ui()

    def __create_ui(self):
        def copy():
            self.execute_command(CopyCommand(self.editor))
        self.copy_button = Button(copy)

        def cut():
            self.execute_command(CutCommand(self.editor))
        self.cut_button = Button(cut)

        def paste():
            self.execute_command(PasteCommand(self.editor))
        self.paste_button = Button(paste)

        self.undo_button = Button(self.undo)

    def execute_command(self, command):
        command.execute()
        self.command_history.append(command)

    def undo(self):
        command = self.command_history.pop()
        if command is not None:
            command.undo()
