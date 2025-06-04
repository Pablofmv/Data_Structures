class Disjointset:

    def __init__(self, n):
        self.parents = list(range(n + 1))
        self.rank = [0] * (n + 1)
    
    def make_set(self, i):
        self.parents[i] = i
        self.rank[i] = 0
    
    def find(self, i):

        if i != self.parents[i]:
            self.parents[i] = self.find(self.parents[i])
        
        return self.parents[i]
    
    def Union(self, i, j):

        i_id = self.find(i)
        j_id = self.find(j)

        if i_id == j_id:
            return 
        
        if self.rank[i_id] > self.rank[j_id]:
            self.parents[j_id] = i_id
        else:
            self.parents[i_id] = j_id
            if self.rank[i_id] == self.rank[j_id]:
                self.rank[j_id] += 1
    
    def __str__(self):
        return " ".join(str(x) for x in self.parents)

if __name__ == "__main__":
    ds = Disjointset(12)

    for i in range(1,13):
        ds.make_set(i)
    
    ds.Union(6, 1)
    ds.Union(6, 11)
    ds.Union(10, 7)
    ds.Union(5, 10)
    ds.Union(5, 3)
    ds.Union(3, 12)
    ds.Union(12, 6)
    ds.Union(3, 2)
    ds.Union(5, 9)
    ds.Union(9, 4)
    ds.Union(12, 8)

    print(ds)