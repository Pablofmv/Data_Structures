
def hash_function(key, m):
    return hash(key) % m

class HashSet:

    def __init__(self, m):
        self.m = m
        self.chains = [[] for i in range(0,m)]
    

    def find(self, key):

        index = hash_function(key, self.m)
        chain = self.chains[index]

        for k in chain:
            if k == key:
                return True
        
        return False
    
    def add(self, key):

        index = hash_function(key, self.m)
        chain = self.chains[index]

        for k in chain:
            if k == key:
                return
        
        chain.append(key)
    
    def eliminate(self, key):

        if not self.find(key):
            return
        
        index = hash_function(key, self.m)
        chain = self.chains[index]

        chain.remove(key)
    

if __name__ == "__main__":

    hs = HashSet(5)

    hs.add("Pablo")
    hs.add("Jorge")
    hs.add("Alex")

    print(hs.chains)

    hs.eliminate("Pablo")
    
    print(hs.chains)

