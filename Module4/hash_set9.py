
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