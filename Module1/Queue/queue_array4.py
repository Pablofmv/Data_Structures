class CirlceQueue:

    def __init__(self, capacity):

        self.capacity = capacity
        self.queue = [None] * capacity
        self.write = 0
        self.read = 0
        self.size = 0
    
    def enqueue(self, item):

        if self.is_full():
            print("Queue is Full")
            return None
        
        self.queue[self.write] = item
        self.write = (self.write + 1) % self.capacity
        self.size += 1
    
    def dequeue(self):

        if self.is_empty():
            print("Queue is Empty")
            return None
        
        item = self.queue[self.read]
        self.queue[self.read] = None
        self.read = (self.read + 1) % self.capacity
        self.size -= 1
        return item
    
    def is_empty(self):
        return self.size == 0
    
    def is_full(self):
        return self.size == self.capacity
    
    def __str__(self):
        return str()
    
if __name__ == "__main__":
    q = CirlceQueue(5)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)



