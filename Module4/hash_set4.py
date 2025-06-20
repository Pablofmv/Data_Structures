
def hash_function(m, key):
    return hash(key) % m


class HashSet:

    def __init__(self, m):
        self.m = m
        self.chains = [[] for i in range(0,m)]
    
    def find(self, m):

        
