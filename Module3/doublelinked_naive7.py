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
        while current and current.key < e:
            current = current.next
        
        if self.head == current and current.key > e:

            new_node.next = current
            current.prev = new_node
            self.head = new_node
            return
        
        if current is None:

            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            return
        
        current.prev.next = new_node
        new_node.prev = current.prev
        new_node.next = current
        current.prev = new_node
    
    def ExtractMax(self):

        if self.head is None:
            return None
        
        max_value = self.tail.key

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        
        return max_value
    
    def PrintPriorityQueue(self):

        current = self.head
        while current:
            print(current.key, end = "->")
            current = current.next
        print("None")


pq = PriorityQueue()
pq.Insert(10)
pq.Insert(20)
pq.Insert(30)
pq.PrintPriorityQueue()
pq.Insert(40)
pq.PrintPriorityQueue()
pq.ExtractMax()
pq.PrintPriorityQueue()
pq.ExtractMax()
pq.PrintPriorityQueue()
        
        

