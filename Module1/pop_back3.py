class Node:
    
    def __init__(self, key):
        self.key = key
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
    
    def pushFront(self, key):

        new_node = Node(key)
        new_node.next = self.head
        self.head = new_node

        if new_node.next is None:
            self.tail = new_node
    
    def pushBack(self, key):

        new_node = Node(key)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def popBack(self):

        if self.head is None:
            raise Exception("Empty List")
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            p = self.head
            while p.next.next is not None:
                p = p.next
            p.next = None
            self.tail = p

    
    def printList(self):
        current = self.head
        while current:
            print(current.key, end = "->")
            current = current.next
        print("None")

if __name__ == "__main__":
    ll = LinkedList()
    ll.pushFront(2)
    ll.pushFront(1)
    ll.pushBack(3)
    ll.printList()
    ll.popBack()
    ll.printList()
    ll.pushBack(3)
    ll.printList()
    ll.popBack()
    ll.printList()