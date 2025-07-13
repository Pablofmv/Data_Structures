# python3
import random

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

class HashWithChains:
        
    def __init__(self, size = 4):
        self.size = 4
        self.p = 10 ** 9 + 7
        self.num_keys = 0
        self.chains = [[] for i in range(0, self.size)]
        self.generate_hash_function()

    def generate_hash_function(self):
        self.a = random.randint(1, self.p - 1)
        self.b = random.randint(0, self.p - 1)
        self.hash = lambda x : ((self.a * x + self.b) % self.p) % self.size
    
    def load_factor(self):
        return self.num_keys / self.size

    def rehash(self):

        if self.load_factor() <= 0.9:
            return
        
        print("Rehashing ...")
        
        old_chain = self.chains
        self.size *= 2
        self.chains = [[] for i in range(0, self.size)]
        self.generate_hash_function()
        self.num_keys = 0

        for chain in old_chain:
            for key, value in chain:
                self.insert(key, value)
    
    def insert(self, key, value):

        index = self.hash(key)
        chain = self.chains[index]

        for i, (k, v) in enumerate(chain):
            if key == k:
                chain[i] = (key, value)
                return
        
        chain.append((key, value))
        self.num_keys += 1
        self.rehash()
    
    def search(self, key):

        index = self.hash(key)
        chain = self.chains[index]

        for k,v in chain:
            if key == k:
                return v
        
        return "not found"
    
    def delete(self, key):

        index = self.hash(key)
        chain = self.chains[index]

        for i, (k,v) in enumerate(chain):

            if key == k:
                del chain[i]
                self.num_keys -= 1
                return
        
        return

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))



def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = HashWithChains()
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            contacts.insert(cur_query.number, cur_query.name)
        elif cur_query.type == 'del':
            contacts.delete(cur_query.number)
        else:
            result.append(contacts.search(cur_query.number))
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

