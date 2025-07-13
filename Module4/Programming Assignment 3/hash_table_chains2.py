import random

class HashTableWithChains:

    def __init__(self, size = 2):
        self.size = size
        self.chains = [[] for i in range(0,size)]
        self.num_keys = 0
        self.p = 10 ** 9 + 17
        self.generate_hash_function()

    def generate_hash_function(self):

        self.a = random.randint(1, self.p - 1)
        self.b = random.randint(0, self.p - 1)
        self.hash = lambda x : ((self.a * x + self.b)% self.p) % self.size
    
    def load_factor(self):
        return self.num_keys / self.size
    
    def rehash(self):

        if self.load_factor() <= 0.9:
            return 
        
        print("Rehashing ...")

        old_chains = self.chains
        self.size *= 2
        self.generate_hash_function()
        self.chains = [[] for i in range(0, self.size)]
        self.num_keys = 0

        for chain in old_chains:
            for key, value in chain:
                self.insert(key, value)
    
    def insert(self, key, value):

        index = self.hash(key)
        chain = self.chains[index]

        for i, (k,v) in enumerate(chain):
            if k == key:
                chain[i] = (key, value)
                return
        
        chain.append((key,value))
        self.num_keys += 1
        self.rehash()
    
    def search(self, key):

        index = self.hash(key)
        chain = self.chains[index]

        for k, v in chain:
            if k == key:
                return v
        
        return None
    
    def delete(self, key):

        index = self.hash(key)
        chain = self.chains[index]

        for i, (k, v) in enumerate(chain):
            if k == key:
                del chain[i]
                self.num_keys -= 1
                return True
        
        return False

if __name__ == "__main__":

    ht = HashTableWithChains()

    ht.insert(1482567, "Alice")
    ht.insert(2031122, "Bob")
    ht.insert(9999999, "Charlie")

    print(ht.search(2031122))  # Output: Bob
    print(ht.search(1482567))  # Output: Alice
    print(ht.search(0000000))  # Output: None

    print(ht.chains)

    ht.delete(2031122)

    print(ht.chains)

    ht.insert(9999998, "Pablo")

                

    
