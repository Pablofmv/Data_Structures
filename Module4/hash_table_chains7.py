import random

class HashTableWithChains:

    def __init__(self, size = 3):
        self.size = size
        self.chains = [[] for i in range(0, self.size)]
        self.num_keys = 0
        self.p = 10000019 #Prime number
        self.generate_hash_funtion()
    
    def generate_hash_funtion(self):
        self.a = random.randint(1, self.p - 1)
        self.b = random.randint(0, self.p - 1)
        self.hash = lambda x : ((self.a * x + self.b) % self.p) % self.size
    
    def load_factor(self):
        return self.num_keys / self.size
    
    def rehash(self):

        if self.load_factor() <= 0.9:
            return
        
        print("Rehashing ...")

        old_chains = self.chains
        self.size *= 2
        self.chains = [[] for i in range(0, self.size)]
        self.num_keys = 0
        self.generate_hash_funtion()

        for chain in old_chains:
            for key,value in chain:
                self.insert(key, value)
        
    
    def insert(self, key, value):

        phone_int = self.convert_to_int(key)
        index = self.hash(phone_int)
        chain = self.chains[index]

        for i, (key,value) in enumerate(chain):
            chain[i] = (key, value)
            return
        
        chain.append((key, value))
        self.num_keys += 1
        self.rehash()
    
    def search(self, key):

        phone_int = self.convert_to_int(key)
        index = self.hash(phone_int)
        chain = self.chains[index]

        for k, v in chain:
            if key == k:
                return v
        
        return None
    
    def convert_to_int(self, phone_number):
        return int("".join(filter(str.isdigit, str(phone_number))))
    
if __name__ == "__main__":

    ht = HashTableWithChains()

    ht.insert("148-25-67", "Alice")
    ht.insert("203-11-22", "Bob")
    ht.insert("999-99-99", "Charlie")

    print(ht.search("203-11-22"))  # Output: Bob
    print(ht.search("148-25-67"))  # Output: Alice
    print(ht.search("000-00-00"))  # Output: None



