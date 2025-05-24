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
    
    def sift_up(self, i):

        while i > 1 and self.H[self.parent(i)] < self.H[i]:
            self.H[self.parent(i)], self.H[i] = self.H[i], self.H[self.parent(i)]
            i = self.parent(i)
    
    def sift_down(self, i):

        maxIndex = i
        left = self.left(i)
        if left <= self.size and self.H[left] > self.H[maxIndex]:
            maxIndex = left
        right = self.right(i)
        if right <= self.size and self.H[right] > self.H[maxIndex]:
            maxIndex = right
        
        if i != maxIndex:
            self.H[i], self.H[maxIndex] = self.H[maxIndex], self.H[i]
            self.sift_down(maxIndex)
    
    def insert(self, p):

        if self.size == self.maxSize :
            return "Error"
        
        self.size += 1
        self.H[self.size] = p
        self.sift_up(self.size)
    
    def extract_max(self):

        if self.size < 1:
            return "Error"
        
        max_value = self.H[1]
        self.H[1] = self.H[self.size]
        self.size -= 1
        self.sift_down(1)

        return max_value
    
    def print(self):
        print(self.H[1:self.size+1])
    
mh = MaxHeap(10)
mh.insert(30)
mh.insert(20)
mh.insert(10)
mh.print()
mh.insert(25)
mh.print()
mh.insert(50)
mh.print()
