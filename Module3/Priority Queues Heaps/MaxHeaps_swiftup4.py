class MaxHeap:

    def __init__(self, maxSize):
        self.H = [0] * (maxSize + 1)
        self.size = 0
        self.maxSize = maxSize
    
    def parent(self, i):
        return i // 2
    
    def left(self, i):
        return i * 2
    
    def right(self, i):
        return i * 2 + 1
    
    def sift_up(self, i):

        while i > 1 and self.H[self.parent(i)] < self.H[i]:
            self.H[self.parent(i)], self.H[i] = self.H[i], self.H[self.parent(i)]
            i = self.parent(i)

    def insert(self, p):

        if self.size == self.maxSize:
            return "ERROR"
        
        self.size += 1
        self.H[self.size] = p
        self.sift_up(self.size)
    
    def sift_down(self, i):

        maxIndex = i 
        l = self.left(i)
        if l <= self.size and self.H[l] > self.H[maxIndex]:
            maxIndex = l
        
        r = self.right(i)
        if r <= self.size and self.H[r] > self.H[maxIndex]:
            maxIndex = r
        
        if i != maxIndex:
            self.H[i], self.H[maxIndex] = self.H[maxIndex], self.H[i]
            self.sift_down(maxIndex)

    def extract_max(self):

        if self.size < 1:
            return None
        
        max_value = self.H[1]
        self.H[1] = self.H[self.size]
        self.size -= 1
        self.sift_down(1)

        return max_value
    
    def print(self):
        print(self.H[1:self.size + 1])

    
    



mh = MaxHeap(10)
mh.insert(30)
mh.insert(20)
mh.insert(10)
mh.print()
mh.insert(50)
mh.print()
mh.extract_max()
mh.print()