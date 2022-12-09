class Component:
    def __init__(self, name):
        self.name = name
        self.parent = None

    def move(self, new_path):
        new_folder = get_path(new_path)
        del self.parent.children[self.name]
        new_folder.children[self.name] = self
        self.parent = new_folder
    
    def delete(self):
        del self.parent.children[self.name]

class Folder(Component):                    # Composite class
    def __init__(self, name):
        super().__init__(name)
        self.children = {}

    def add_child(self, child):
        child.parent = self
        self.children[child.name] = child

    def copy(self, new_path):
        f = Folder(self.name)
        f.parent = new_path
        for child in self.children:
            child.copy()

class File(Component):                      # Leaf class
    def __init__(self, name, contents):
        super().__init__(name)
        self.contents = contents

    def copy(self, new_path):
        f = File(self.name, self.contents)
        f.parent = new_path




root = Folder("")

def get_path(path):
    names = path.split("/")[1:]
    node = root
    for name in names:
        node = node.children[name]
    return node