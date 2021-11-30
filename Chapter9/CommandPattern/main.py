import sys


class Window:
    def exit(self):
        sys.exit(0)


class Document:
    def __init__(self, filename):
        self.filename = filename
        self.contents = "This file cannot be modified"

    def save(self):
        with open(self.filename, "w") as file:
            file.write(self.contents)


class ToolbarButton:
    def __init__(self, name, iconname):
        self.name = name
        self.iconname = iconname

    def click(self):
        self.command.execute()


class MenuItem:
    def __init__(self, menu_name, menuitem_name):
        self.menu = menu_name
        self.item = menuitem_name

    def click(self):
        self.command.execute()


class KeyboardShortcut:
    def __init__(self, key, modifier):
        self.key = key
        self.modifier = modifier

    def keypress(self):
        self.command.execute()


class SaveCommand:
    def __init__(self, document):
        self.document = document

    def execute(self):
        self.document.save()


class ExitCommand:
    def __init__(self, window):
        self.window = window

    def execute(self):
        self.window.exit()


if __name__ == '__main__':
    # Receivers
    window = Window()
    document = Document("a_document.txt")
    # Commands
    save = SaveCommand(document)
    exit = ExitCommand(window)

    # Invokers
    save_button = ToolbarButton("save", "save.png")
    save_keystroke = KeyboardShortcut("s", "ctrl")
    exit_menu = MenuItem("File", "Exit")

    # Setting the commands on the invokers
    save_button.command = save
    save_keystroke.command = save
    exit_menu.command = exit

    # You ( the client ) invoke the invokers that invoke the commands that interact with the receivers