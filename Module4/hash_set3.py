
def hash_function(m, key):
    return hash(key) % m

class HashSet:

    def __init__(self, m):

        self.m = m
        self.chains = [[] for i in range(0,m)]

    
    def find(self, key):

        index = hash_function(self.m, key)
        chain = self.chains[index]

        if key in chain:
            return True
        
        return False
    
    def add(self, key):

        index = hash_function(self.m, key)
        chain = self.chains[index]

        if key in chain:
            return
        
        self.chains[index].append(key)
    
    def remove(self, key):

        index = hash_function(self.m, key)
        chain = self.chains[index]

        if not self.find(key):
            return
        
        self.chains[index].remove(key)

if __name__ == "__main__":

    hs = HashSet(5)

    hs.add("Alice")
    hs.add("Bob")
    hs.add("Charlie")

    print(hs.find("Bob"))
    print(hs.find("Pablo"))

    hs.add("Bob")
    print(hs.chains)
    hs.remove("Alice")
    print(hs.chains)
    print(hs.find("Alice"))