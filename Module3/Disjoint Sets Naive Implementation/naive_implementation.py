class DisjoinSet:

    def __init__(self, n):
        self.smallest = list(range(n+1))
    
    def make_set(self, i):
        self.smallest[i] = i
    
    def find(self, i):
        return self.smallest[i]
    
    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)

        if i_id == j_id:
            return
        
        new_id = min(i_id, j_id)

        for k in range(1, len(self.smallest)):
            if self.smallest[k] == i_id or self.smallest[k] == j_id:
                self.smallest[k] = new_id
    
    def __str__(self):
        return " ".join(str(x) for x in self.smallest[1:])

if __name__ == "__main__":

    ds = DisjoinSet(9)

    print(ds)

    for i in range(1,10):
        ds.make_set(i)
    print(ds)

    ds.union(9,3)
    print(ds)

    ds.union(3,2)
    print(ds)