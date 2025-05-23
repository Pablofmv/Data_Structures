class MaxHeap:

    def __init__(self, maxSize):

        self.H = [0] * (maxSize + 1)
        self.size = 0
        self.maxSize = maxSize
    
    def parent(self, i):
        return i // 2
    
    def left(self, i):
        return 2 * i
    
    def right(self, i):
        return 2 * i + 1

    def insert(self, p):
        if self.size == self.maxSize:
            return "Error"
        
        self.size += 1
        self.H[self.size] = p
        self.sift_up(self.size)
    
    def sift_up(self, i):

        while i > 1 and self.H[self.parent(i)] < self.H[i]:
            self.H[self.parent(i)], self.H[i] = self.H[i], self.H[self.parent(i)]
            i = self.parent(i)


heap = MaxHeap(10)
heap.insert(10)
heap.insert(20)
heap.insert(5)

print(heap.H)

heap.insert(30)

print(heap.H)
