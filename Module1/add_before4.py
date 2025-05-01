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

        if self.tail is None:
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
            raise Exception("Empty List.")
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            p = self.head
            while p.next.next is not None:
                p = p.next
            p.next = None
            self.tail = p
        
    def popFront(self):

        if self.head is None:
            raise Exception("Empty List.")
        
        self.head = self.head.next

        if self.head is None:
            self.tail = None
    
    def AddAfter(self, node, key):

        new_node = Node(key)
        new_node.next = node.next
        node.next = new_node

        if self.tail == node:
            self.tail = new_node
    
    def AddAfterKey(self, target_key, new_key):

        if self.head is None:
            print(f"Empty List.")
            return
        
        current = self.head
        while current and current.key != target_key:
            current = current.next
        
        if current:
            self.AddAfter(current,new_key)
        else:
            print(f"Node with key {target_key} is not found.")


    def AddBeforeKey(self, target_key, new_key):

        if self.head is None:
            print("Empty List.")
            return
        
        if self.head.key == target_key:
            self.pushFront(new_key)
            return

        current = self.head
        while current.next and current.next.key != target_key:
            current = current.next
        
        if current.next:
            new_node = Node(new_key)
            new_node.next = current.next
            current.next = new_node
        else:
            print(f"Node with key {target_key} is not found.")


    
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
    ll.popFront()
    ll.printList()
    ll.AddAfterKey(2,3)
    ll.printList()
    ll.AddBeforeKey(2,1)
    ll.printList()