class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def pushFront(self, key):

        new_node = Node(key)

        new_node.next = self.head

        self.head = new_node
    
    def printList(self):
        current = self.head
        while current:
            print(current.key, end = "->")
            current = current.next
        print("None")

if __name__ == "__main__":
    ll = LinkedList()
    ll.pushFront(1)
    ll.pushFront(2)
    ll.printList()

