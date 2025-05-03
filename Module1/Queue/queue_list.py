class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size =0

    def enqueue(self, key):
        new_node = Node(key)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.size +=1
    
    def dequeue(self):

        if self.is_empty():
            print("Empty List!")
            return None
        
        item = self.head.key
        self.head = self.head.next

        if self.head is None:
            self.tail = None
        
        self.size -= 1

        return item
    
    def is_empty(self):
        return self.size == 0
    
    def printList(self):
        current = self.head
        while current:
            print(current.key, end = "->")
            current = current.next
        print("None")
    
if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.printList()
    q.dequeue()
    q.printList()
    q.dequeue()
    q.printList()
    q.enqueue(4)
    q.printList()
