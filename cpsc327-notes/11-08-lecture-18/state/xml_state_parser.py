import abc

class Node:
    def __init__(self, tag_name, parent=None):
        self.parent = parent
        self.tag_name = tag_name
        self.children = []
        self.text = ""

    def __str__(self):
        if self.text:
            return self.tag_name + ": " + self.text
        else:
            return self.tag_name

class XmlState(metaclass=abc.ABCMeta):
    """
    This is a singleton and every time you "create an XmlState" it gives you a single instance rather than creating a new one"""
    @abc.abstractmethod
    def process():
        pass

    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance  = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def get_instance(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance  = cls(*args, **kwargs)
        return cls._instance

class FirstTag(XmlState):
    def process(self, remaining_string, parser):
        i_start_tag = remaining_string.find("<")
        i_end_tag = remaining_string.find(">")
        tag_name = remaining_string[i_start_tag + 1 : i_end_tag]
        root = Node(tag_name)
        parser.root = parser.current_node = root
        parser.state = ChildNode.get_instance()
        return remaining_string[i_end_tag + 1 :]


class ChildNode(XmlState):
    def process(self, remaining_string, parser):
        stripped = remaining_string.strip()
        if stripped.startswith("</"):
            parser.state = CloseTag()
        elif stripped.startswith("<"):
            parser.state = OpenTag()
        else:
            parser.state = TextNode()
        return stripped


class OpenTag(XmlState):
    def process(self, remaining_string, parser):
        i_start_tag = remaining_string.find("<")
        i_end_tag = remaining_string.find(">")
        tag_name = remaining_string[i_start_tag + 1 : i_end_tag]
        node = Node(tag_name, parser.current_node)
        parser.current_node.children.append(node)
        parser.current_node = node
        parser.state = ChildNode()
        return remaining_string[i_end_tag + 1 :]


class CloseTag(XmlState):
    def process(self, remaining_string, parser):
        i_start_tag = remaining_string.find("<")
        i_end_tag = remaining_string.find(">")
        assert remaining_string[i_start_tag + 1] == "/"
        tag_name = remaining_string[i_start_tag + 2 : i_end_tag]
        assert tag_name == parser.current_node.tag_name
        parser.current_node = parser.current_node.parent
        parser.state = ChildNode()
        return remaining_string[i_end_tag + 1 :].strip()


class TextNode(XmlState):
    def process(self, remaining_string, parser):
        i_start_tag = remaining_string.find("<")
        text = remaining_string[:i_start_tag]
        parser.current_node.text = text
        parser.state = ChildNode()
        return remaining_string[i_start_tag:]



class Parser:
    def __init__(self, parse_string):
        self.parse_string = parse_string
        self.root = None
        self.current_node = None

        self.state = FirstTag()

    def parser_process(self, remaining_string):
        remaining = self.state.process(remaining_string, self)  # pass Parser to the state;
                                                                # so that the state can handle state updates
        if remaining:
            self.parser_process(remaining)

    def start(self):
        self.parser_process(self.parse_string)


if __name__ == "__main__":
    import sys

    with open(sys.argv[1]) as file:
        contents = file.read()
        p = Parser(contents)
        p.start()

        nodes = [p.root]
        while nodes:
            node = nodes.pop(0)
            print(node)
            nodes = node.children + nodes
