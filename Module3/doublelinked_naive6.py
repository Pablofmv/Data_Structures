class Node:

    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None

class PriorityQueue:

    def __init__(self):
        self.head = 0
        self.tail = 0

    def Insert(self, e):

        new_node = Node(e)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        
        current = self.head
        while current is not None and current.key < e:
            current = current.next