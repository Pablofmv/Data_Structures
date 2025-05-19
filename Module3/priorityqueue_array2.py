class PriorityQueue:

    def __init__(self):
        self.arr = []

    def Extract(self):

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

        for i in range(len(self.arr)-1,left, -1):
            self.arr[i+1] = self.arr[i]
        
        self.arr[left] = e

    def Print(self):

        print(self.arr)

pq = PriorityQueue()
for value in [1,2,3,4,5,6,7,8,9]:
    pq.Insert(value)

pq.Print()

pq.Insert(5.5)

pq.Print()



