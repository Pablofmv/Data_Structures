class Node:

    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None

class PriorityQueue:

    def __init__(self):
        self.head = None
        self.tail = None
    
    def Insert(self, e):

        new_node = Node(e)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        
        current = self.head
        while current is not None and current.key < e:
            current = current.next
        
        if current == self.head and current.key > e:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            if new_node.next is None:
                self.tail = new_node
            return
        
        if current is None:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            return
        
        new_node.prev = current.prev
        new_node.next = current.next
        current.prev.next = new_node
        current.prev = new_node

    def ExtractMax(self):

        if self.tail is None:
            return None
        
        max_value = self.tail.key

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        
        return max_value
    
    def PrintLinkedList(self):

        current = self.head
        while current:
            print(current.key, end = "->")
            current = current.next
        print("None")

pq = PriorityQueue()
pq.Insert(10)
pq.Insert(20)
pq.Insert(30)

pq.PrintLinkedList()

pq.ExtractMax()

pq.PrintLinkedList()
