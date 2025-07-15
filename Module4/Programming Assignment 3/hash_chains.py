# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = [([], set()) for i in range(0, self.bucket_count)]
        self.solution = []

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):

        if query.type == "add":
            # use reverse order, because we append strings to the end
            index = self._hash_func(query.s)
            chain, s = self.elems[index]

            if query.s not in s:
                chain.insert(0, query.s)
                s.add(query.s)
        
        elif query.type == "find":

            index = self._hash_func(query.s)
            chain, s = self.elems[index]

            if query.s in s:
                self.solution.append("yes")
            else:
                self.solution.append("no")
        
        elif query.type == "check":

            chain,_ = self.elems[query.ind]
            self.solution.append(' '.join(chain))
        
        elif query.type == "del":

            index = self._hash_func(query.s)
            chain, s = self.elems[index]

            if query.s in s:
                chain.remove(query.s)
                s.remove(query.s)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())
        
        for word in self.solution:
            print(word)

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
