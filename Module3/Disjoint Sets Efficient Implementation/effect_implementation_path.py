class DisjointSet:

    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = list(range(n + 1))
    
    def make_set(self, i):
        self.parent[i] = i
    
    def find(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        
        return self.parent[i]
    
    def union(self, i, j):

        i_dj = self.find(i)
        j_dj = self.find(j)

        if i_dj == j_dj:
            return 
        
        if self.rank[i_dj] > self.rank[j_dj]:
            self.parent[j_dj] = i_dj
        else:
            self.parent[i_dj] = j_dj

            if self.rank[i_dj] == self.rank[j_dj]:
                self.rank[j_dj] += 1
    
    def __str__(self):
        return " ".join(str(x) for x in self.parent[1:])

if __name__ == "__main__":

    ds = DisjointSet(5)

    for i in range(1,6):
        ds.make_set(i)
    
    print(ds)

    ds.union(1,4)
    ds.union(4,3)
    ds.union(3,2)

    print(ds)
