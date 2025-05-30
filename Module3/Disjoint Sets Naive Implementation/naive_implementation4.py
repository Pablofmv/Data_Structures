class DisjointSet:

    def __init__(self, n):
        self.smallest = list(range(n+1))
    
    def make_set(self, i):
        self.smallest[i] = i
    
    def find(self, i):
        return self.smallest[i]
    
    def union(self, i, j):

        i_dj = self.find(i)
        j_dj = self.find(j)

        if i_dj == j_dj:
            return
        
        new_dj = min(i_dj,j_dj)
        
        for k in range(0,len(self.smallest)):
            if self.smallest[k] == i_dj or self.smallest[k] == j_dj:
                self.smallest[k] = new_dj
    

    def __str__(self):
        return " ".join(str(x) for x in self.smallest[1:])

if __name__ == "__main__":
    ds = DisjointSet(9)

    for i in range(1, 10):
        ds.make_set(i)
    
    print(ds)

    ds.union(2,3)

    print(ds)

