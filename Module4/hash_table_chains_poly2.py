import random

class HashTableWithChains:

    def __init__(self, size = 1000):
        self.size = size
        self.p = 10000019 #first prime number
        self.x = random.randint(1, self.p-1)
        self.chains = [[]for i in range(0,self.size)]
    
    def poly_hash(self, s):
        hash_value = 0
        for char in reversed(s):
            hash_value = (hash_value * self.x + ord(char)) % self.p
        return hash_value % self.size
    
    def insert(self, name, phone_number):

        index = self.poly_hash(name)
        chain = self.chains[index]

        for i, (k,v) in enumerate(chain):
            if name == k:
                chain[i] = (name, phone_number)
                return
        
        chain.append((name, phone_number))
    
    def search(self, name):

        index = self.poly_hash(name)
        chain = self.chains[index]

        for k,v in chain:
            if name == k:
                return v
        
        return None
    
if __name__ == "__main__":

    ht = HashTableWithChains()

    ht.insert("Alice", "123-4567")
    ht.insert("Bob", "987-6543")
    ht.insert("Charlie","555-1234")

    print(ht.search("Bob"))

    ht.insert("Bob", "000-0000")

    print(ht.search("Bob"))