class Node:

    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
    
def find(k, root):

    if root is None:
        return None
    
    if root.key == k:
        return root
    elif root.key < k:
        return find(k, root.left)
    else:
        return find(k, root.right)
    
def next_node(N):

    if N.right:
        return left_descendant(N.right)
    else:
        return right_ancestor(N)

def left_descendant(N):
    while N.left:
        N = N.left
    return N    

def right_ancestor(N):
    
    