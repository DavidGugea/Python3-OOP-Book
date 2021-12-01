class Component:
    def __init__(self, name):
        self.name = name

    def move(self, new_path):
        new_folder = get_path(new_path)
        del self.parent.children[self.name]
        new_folder.children[self.name] = self
        self.parent = new_folder

    def delete(self):
        del self.parent.children[self.name]


class Folder(Component):
    def __init__(self, name):
        super().__init__(name)
        self.children = {}

    def add_child(self, child):
        child.parent = self
        self.children[child.name] = child

    def move(self, new_path):
        pass

    def copy(self, new_path):
        pass

    def delete(self):
        pass


class File(Component):
    def __init__(self, name, contents):
        super().__init__(name)
        self.contents = contents

    def move(self, new_path):
        pass

    def copy(self, new_path):
        pass

    def delete(self):
        pass

root = Folder("")
def get_path(path):
    names = path.split("/")[1:]
    node = root
    for name in names:
        node = node.children[name]

    return node