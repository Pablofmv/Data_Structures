class Node:

    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
    
    def pushBack(self, key):

        new_node = Node(key)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        
    def popBack(self):

        if self.tail is None:
            print("Empty List.")
            return
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
    
    def AddAfter(self, node, key):

        new_node = Node(key)
        new_node.next = node.next
        node.next = new_node
        new_node.prev = node

        if self.tail == node:
            self.tail = new_node
    
    def AddAfterKey(self, target_key, new_key):

        if self.head is None:
            print("Empty List.")
            return
        
        current = self.head
        while current and current.key != target_key:
            current = current.next
        
        if current:
            self.AddAfter(current, new_key)
        else:
            print("Node with key {target_key} not found.")
    
    def printList(self):

        current = self.head
        while current:
            print(current.key, end = "->")
            current = current.next
        print("None")

if __name__ == "__main__":
    ll = DoublyLinkedList()
    ll.pushBack(1)
    ll.pushBack(2)
    ll.pushBack(3)
    ll.printList()
    ll.popBack()
    ll.printList()
    ll.AddAfterKey(2,3)
    ll.printList()


