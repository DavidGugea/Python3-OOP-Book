class Node:
    def __init__(self, tag_name, parent=None):
        self.parent = parent
        self.tag_name = tag_name
        self.children = []
        self.text = ""

    def __str__(self):
        if self.text:
            return "{0}: {1}".format(self.tag_name, self.text)
        else:
            return self.tag_name
