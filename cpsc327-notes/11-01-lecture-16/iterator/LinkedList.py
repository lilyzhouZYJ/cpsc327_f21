class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListIterator:               # Iterator
    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):                 # next
        if not self.current:
            raise StopIteration         # raise StopIteration
        else:
            item = self.current.data
            self.current = self.current.next
            return item

class LinkedList:                       # Iterable object
    def __init__(self):
        self.head = None

    def __iter__(self):                 # iter
        return LinkedListIterator(self.head)

    def add(self, item): 
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

test_list = LinkedList()
test_list.add(1)
test_list.add(2)
test_list.add(3)
for item in test_list:
    print(item)