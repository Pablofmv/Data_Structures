# python3

import sys
import threading


def compute_height(n, parents):
    # Replace this code with a faster implementation
    
    children = [[] for i in range(0,n)]
    root = 0

    for i in range(0,n):
        parent = parents[i]

        if parent == -1:
            root = i
        else:
            children[parent].append(i)

    def dfs(node):

        if not children[node]:
            return 1
        
        tallest_height_node = 0

        for child in children[node]:
            height_node = dfs(child)
            tallest_height_node = max(tallest_height_node, height_node)
        
        return tallest_height_node + 1
    
    return dfs(root)



def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
