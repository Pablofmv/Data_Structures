class Node:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.size = 1
        self.height = 0

def height(n):
    return n.height if n else 0

def size(n):
    return n.size if n else -1

def update_height(n):
    n.height = 1 + max(height(n.left), height(n.right))
