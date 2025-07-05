import random

class HashTableWithChains:

    def __init__(self, size = 1000):

        self.size = size
        self.p = 10000019 #prime number
        self.chains = [[] for i in range(0,size)]
        self.x = random.randint(1, self.p - 1)
    
    def poly_hash(self, s):
        hash_value = 0
        for char in reversed(s):
            hash_value = (hash_value * self.x + ord(char)) % self.p
        return hash_value % self.size
    
    def insert(self, key, value):

        index = self.poly_hash(key)
        chain = self.chains[index]

        for i, (k, v) in chain:
            if key == k:
                return v
        
        chain.append((key, value))
    
    def search(self, key):

        index = self.poly_hash(key)
        chain = self.chains[index]

        for k, v in chain:
            if key == k:
                return v
        
        return None

if __name__ == "__main__":

    ht = HashTableWithChains()

    ht.insert("Alice", "123-4567")
    ht.insert("Bob", "987-6543")
    ht.insert("Charlie", "555-1234")

    print(ht.search("Alice"))    # → 123-4567
    print(ht.search("Bob"))      # → 987-6543
    print(ht.search("Charlie"))  # → 555-1234

            