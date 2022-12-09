class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):             # returns generator (which is a type of iterator)
        current = self.head
        while current is not None:
            yield current.data      # "returns" data,
                                    # but when next() is called, will start here again
            current = current.next

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