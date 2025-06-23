
def hash_function(key, m):
    return hash(key) % m

class HashSet:

    def __init__(self, m):
        self.m = m
        self.chains = [[] for i in range(0,m)]
    
    
    def find(self, key):

        index = hash_function(key, self.m)
        chain = self.chains[index]

        if key in chain:
            return True
        
        return False
    
    def add(self, key):

        index = hash_function(key, self.m)
        chain = self.chains[index]

        if key in chain:
            return
        
        chain.append(key)
    
    def remove(self, key):

        if not self.find(key):
            return 
        
        index = hash_function(key, self.m)
        chain = self.chains[index]

        chain.remove(key)
    
if __name__ == "__main__":

    hs = HashSet(5)
    
    hs.add("Pablo")
    hs.add("Sunil")

    print(hs.chains)

    print(hs.find("Pablo"))

    hs.remove("Pablo")

    print(hs.chains)

        