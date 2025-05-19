class PriorityQueueArray:

    def __init__(self):
        self.arr = []

    def ExtractMax(self):
        
        if not self.arr:
            return None
        
        return self.arr.pop()
    
    def Insert(self, e):

        left, right = 0, len(self.arr)
        while left < right:
            mid = (left + right) // 2
            if self.arr[mid] < e:
                left = mid + 1
            else:
                right = mid
        
        self.arr.append(None)

        for i in range(len(self.arr) - 1, left, -1):
            self.arr[i] = self.arr[i - 1]
        
        self.arr[left] = e
    
    def display(self):
        print(self.arr)

pq = PriorityQueueArray()

for value in [0,1,2,3,4,5,6,7,8,9]:
    pq.Insert(value)

pq.display()

pq.Insert(5.5)

pq.display()

pq.ExtractMax()

pq.display()
