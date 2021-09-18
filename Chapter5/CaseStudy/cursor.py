from character import Character

class Cursor:
    def __init__(self, document):
        self.document = document
        self.position = 0

    def forward(self):
        self.position += 1

    def back(self):
        self.position -= 1

    def is_file_empty(self):
        return not bool(self.document.characters)

    def home(self):
        if self.is_file_empty():
            return

        while self.document.characters[self.position - 1].character != '\n':
            self.position -= 1

            if self.position == 0:
                # Got to beginning of file before newline
                break

    def end(self):
        if self.is_file_empty():
            return

        while self.position < len(self.document.characters) and self.document.characters[self.position].character != '\n':
            self.position += 1