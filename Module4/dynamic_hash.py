import random

class HashTable:

    def __init__(self, size = 8):
        self.size = size
        self.count = 0
        self.chains = [[] for i in range(0,self.size)]

    
    def hash(self, key):
        return hash(key) % self.size
    
    def load_factor(self):
        return self.count / self.size
    
    def rehash(self):
        if self.load_factor() <= 0.9:
            return
        
        old_chains = self.chains
        self.size *= 2
        self.chains = [[] for i in range(0,self.size)]
        self.count = 0

        for chain in old_chains:
            for key,value in chain:
                self.insert(key,value)
            
    
    def insert(self, key, value):
        index = self.hash(key)
        chain = self.chains[index]

        for i, (k,v) in enumerate(chain):
            if k == key:
                chain[i] = (key, value)
                return
        
        chain.append((key,value))
        self.count += 1
        self.rehash()
    
    def get(self, key):
        index = self.hash(key)
        chain = self.chains[index]
        
        for k,v in chain:
            if k == key:
                return v
        
        return None
    
    def remove(self, key):
        index = self.hash(key)
        chain = self.chains[index]

        for i , (k,v) in enumerate(chain):
            if k == key:
                del chain[i]
                self.count -= 1
                return
    
    def display(self):
        for i, chain in enumerate(self.chains):
            print(f"{i} : {chain}")

ht = HashTable()

for i in range(0,20):
    ht.insert(f"key{i}",i)

ht.display()

print(ht.get("key5"))

