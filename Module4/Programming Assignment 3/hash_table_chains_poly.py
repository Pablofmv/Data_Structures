import random

class HashTableWithChains:

    def __init__(self, size = 4):
        self.size = size
        self.chains = [[] for i in range(0, self.size)]
        self.p = 10 ** 7 + 19
        self.x = random.randint(1, self.p - 1)

    
    def poly_hash(self, key):
        hash_value = 0
        for c in reversed(key):
            hash_value = (hash_value * self.x + ord(c)) % self.p
        return hash_value
    
    def add(self, key):

        index = self.poly_hash(key) % self.size
        chain = self.chains[index]

        for k in chain:
            if k == key:
                return
        
        chain.append(key)
    
    def find(self, key):

        index = self.poly_hash(key) % self.size
        chain = self.chains[index]

        for k in chain:
            if k == key:
                return "yes"
        
        return "no"

    def checki(self, i):

        if 0 <= i <= len(self.chains):
            return " ".join(element for element in self.chains[i])
        
        return " "
    
    def delete (self, key):

        index = self.poly_hash(key) % self.size
        chain = self.chains[index]

        for i, k in enumerate(chain):
            if k == key:
                chain.remove(key)
                return
        
        return

if __name__ == "__main__":

    ht = HashTableWithChains()
    ht.add("apple")
    ht.add("banana")
    ht.add("grape")

    print(ht.chains)
    ht.delete("banana")
    print(ht.chains)
    


