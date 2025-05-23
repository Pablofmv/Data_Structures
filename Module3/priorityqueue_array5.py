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
            self.arr[i] = self.arr[i-1]
        
        self.arr[left] = e
    
    def PrintQueue(self):
        print(self.arr)
    

pq = PriorityQueueArray()
pq.ExtractMax()
pq.PrintQueue()
for value in [1,2,3,4,5]:
    pq.Insert(value)

pq.PrintQueue()
pq.Insert(3.5)
pq.PrintQueue()