class DisjointSet:

    def __init__(self, n):
        self.parent = list(range(n+1))
        self.rank =[0] * (n+1)
    
    def make_set(self, i):
        self.parent[i] = i
        self.rank[i] = 0
    
    def find(self, i):
        while i != self.parent[i]:
            i = self.parent[i]
        
        return i
    
    def union(self, i, j):
        i_dj = self.find(i)
        j_dj = self.find(j)

        if i_dj == j_dj:
            return
        
        if i_dj > j_dj:
            self.parent[j_dj] = i_dj
        else:
            self.parent[i_dj] = j_dj
            if self.rank[i_dj] == self.rank[j_dj]:
                self.rank[j_dj] += 1
    
    def __str__(self):
        return ' '.join(str(x) for x in self.parent[1:])

if __name__ == "__main__":

    ds = DisjointSet(5)
    for i in range(1,6):
        ds.make_set(i)
    
    ds.union(1,4)
    ds.union(4,3)
    ds.union(3,2)

    print(ds)

    print(f"Are 1 and 5 connected: {ds.find(1) == ds.find(5)}")