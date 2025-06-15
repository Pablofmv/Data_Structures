
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
            if key == k:
                return True
        
        return False
    
    def add(self, key):

        index = hash_function(key, self.m)
        chain = self.chains[index]

        for k in chain:
            if k == key:
                return None
        
        chain.append(key)
    
    def remove(self, key):

        if not self.find(key):
            return 
        
        index = hash_function(key, self.m)
        chain = self.chains[index]
        chain.remove(key)
    
if __name__ == "__main__":

    s = HashSet(5)

    s.add("Alice")
    s.add("Bob")
    s.add("Charlie")

    print(s.find("Bob"))
    print(s.find("David"))

    s.add("Bob")
    print(s.chains)
    s.add("Alice")
    print(s.chains)
    s.remove("Alice")
    print(s.chains)