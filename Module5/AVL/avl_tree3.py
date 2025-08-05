class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0
    
def height(n):
    return n.height if n else -1

def update_height(n):
    n.height = 1 + max(height(n.left), height(n.right))

def get_balance(n):
    return height(n.left) - height(n.right)

def rotate_left(x):
    y = x.right
    x.right = y.left
    if y.left:
        y.left.parent = x
    y.left = x

    y.parent = x.parent
    x.parent = y

    update_height(x)
    update_height(y)
    return y


