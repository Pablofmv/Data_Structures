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