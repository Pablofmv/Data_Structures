
def hash_function(key, m):
    return hash(key) % m

class HashMap:

    def __init__(self, m):
        self.m = m
        self.chains = [[] for _ in range(m)]

    def has_key(self, key):

        index = hash_function(key, self.m)
        chain = self.chains[index]
        for k, v in chain:
            if k == key:
                return True
        
        return False
    
    def get(self, key):
        index = hash_function(key, self.m)
        chain = self.chains[index]
        for k, v in chain:
            if k == key:
                return v
        
        return None
    
    def set(self, key, value):
        index = hash_function(key, self.m)
        chain = self.chains[index]

        for i, (k, v) in enumerate(chain):
            if k == key:
                chain[i] = (key, value)
                return
        chain.append((key, value))

if __name__ == "__main__":
    phone_book = HashMap(5)

    phone_book.set("Maria", "01707773331")
    phone_book.set("Helen", "15025757575")
    phone_book.set("Sasha", "14052391717")

    print(phone_book.get("Maria"))
    print(phone_book.get("Pablo"))