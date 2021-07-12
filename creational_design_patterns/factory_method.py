class Button:
    def render(self) -> str:
        raise NotImplementedError

    def on_click(self):
        raise NotImplementedError


class Dialog:
    content = ''
    button = None

    def create_button(self) -> Button:
        raise NotImplementedError

    def render(self):
        self.button = self.create_button()
        self.content = self.button.render()


class WindowsButton(Button):
    def render(self):
        return 'Windows Button'

    def on_click(self):
        return 'Windows Button On Click'


class WindowsDialog(Dialog):
    def create_button(self) -> Button:
        button = WindowsButton()
        return button


class HtmlButton(Button):
    def render(self):
        return 'Html Button'

    def on_click(self):
        return 'Html Button On Click'


class WebDialog(Dialog):
    def create_button(self) -> Button:
        button = HtmlButton()
        return button


class Application:
    dialog = None
    message = None

    def __init__(self, os):
        if os == 'Windows':
            self.dialog = WindowsDialog()
        elif os == 'Web':
            self.dialog = WebDialog()
        else:
            raise Exception(f'os: {os} is not supported')

        self.dialog.render()

    def click_button(self):
        self.message = self.dialog.button.on_click()
