class DynamicArray:

    def __init__(self):
        self.arr = [None] * 1
        self.capacity = 1
        self.size = 0
    
    def Get(self, i):

        if i < 0 or i >= self.size:
            raise IndexError("Index out of range.")
        
        return self.arr[i]
    
    def Set(self, i, value):

        if i < 0 or i >= self.size:
            raise IndexError("Index out of range.")
        
        self.arr[i] = value

    def PushBack(self, value):

        if self.capacity == self.size:
            new_arr = [None] * (2 * self.capacity)

            for i in range(0,self.size):
                new_arr[i] = self.arr[i]
            
            self.capacity = 2 * self.capacity
            self.arr = new_arr
        
        self.arr[self.size] = value
        self.size += 1

    def Remove(self, i):

        if i < 0 or i >= self.size:
            raise IndexError("Index out of range.")
        
        for j in range(i, self.size - 1):
            self.arr[j] = self.arr[ j + 1]
        
        self.arr[self.size - 1] = None
        self.size -= 1

    def Size(self):
        return self.size

da = DynamicArray()
da.PushBack(0)
da.PushBack(1)
da.PushBack(2)
da.PushBack(3)

print(da.arr)

da.Remove(2)

print(da.arr)
