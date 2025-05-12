class DynamicArray:

    def __init__(self):
        self.arr = [None] * 1
        self.size = 0
        self.capacity = 1

    def Get(self, i):

        if i < 0 or i >= self.size:
            raise IndexError("Index out of range.")
        
        return self.arr[i]
    
    def Set(self, i, value):

        if i < 0 or i >= self.size:
            raise IndexError("Index out of range.")

        self.arr[i] = value

        return self.arr[i]
    
    def PushBack(self, value):

        if self.size == self.capacity:

            new_arr = [None] * (2 * self.capacity)

            for i in range(0,self.size):
                new_arr[i] = self.arr[i]
            
            self.arr = new_arr
            self.capacity = self.capacity * 2
        
        self.arr[self.size] =  value
        self.size += 1
    
    def Remove(self, i):

        if i < 0 or i > self.size:
            raise Exception("Index out of range.")
        
        for j in range(i, self.size - 1):
            self.arr[j] = self.arr[j + 1]

        self.arr[self.size -1] = None
        self.size -= 1

    def Size(self):
        return self.size

da = DynamicArray()

da.PushBack(10)
da.PushBack(20)
da.PushBack(30)

print(da.arr)

da.Remove(0)

print(da.arr)
        
