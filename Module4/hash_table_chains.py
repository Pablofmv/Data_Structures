

class HashTableWithCahins:

    def __init__(self, size = 8):
        self.size = size
        self.chains = [[] for i in range(0,size)]
        self.num_keys = 0
        self.p = 10000019
        self.generate_hash_function()
