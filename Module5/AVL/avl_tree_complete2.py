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
    n.height = 1 + max(height(n.left),height(n.right))

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

def rotate_right(y):

    x = y.left
    y.left = x.right

    if x.right:
        x.right.parent = y
    x.right = y

    y.parent = x.parent
    x.parent = y

    update_height(y)
    update_height(x)

    return x

def rebalance(n):
    update_height(n)
    balance = get_balance(n)

    if balance > 1:
        if get_balance(n.left) < 0:
            n.left = rotate_left(n.left)
        return rotate_right(n)
    
    if balance < -1:
        if get_balance(n.right) > 0:
            n.right = rotate_right(n.right)
        return rotate_left(n)
    
    return n

def insert(root, key):
    if not root:
        return Node(key)
    
    if key < root.key:
        root.left = insert(root.left, key)
        root.left.parent = root
    else:
        root.right = insert(root.right, key)
        root.right.parent = root
    
    return rebalance(root)

def inorder(n):
    if n:
        inorder(n.left)
        print(f"{n.key}(h={n.height})", end = " ")
        inorder(n.right)


def find_max(node):
    while node.right:
        node = node.right
    return node

def delete(root, key):

    if not root:
        return None
    
    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        
        temp = find_max(root.left)
        root.key = temp.key
        root.left = delete(root.left, temp.key)
    return rebalance(root)

def merge_with_root(R1, R2, T):
    T.left = R1
    if R1:
        R1.parent = T
    
    T.right = R2
    if R2:
        R2.parent = T

    update_height(T)
    return rebalance(T)

def merge(R1, R2):
    if not R1:
        return R2
    if not R2:
        return R1
    T = find_max(R1)
    R1 = delete(R1, T.key)
    return merge_with_root(R1, R2, T)

def split(R, x):
    if not R:
        return (None, None)
    if x < R.key:
        L, R1 = split(R.left, x)
        new_right = merge_with_root(R1, R.right, R)
        return (L, new_right)
    else:
        L1, R2 = split(R.right, x)
        new_left = merge_with_root(R.left, L1, R)
    return (new_left, R2)

root = None
for k in [10, 20, 30, 40, 50, 25]:
    root = insert(root, k)

# Inorder print
print("Inorder traversal (sorted):")
inorder(root)

# Split at 30
print("\n\nSplit at 30:")
L, R = split(root, 30)
print("Left (<30):")
inorder(L)
print("\nRight (>30):")
inorder(R)

# Merge back
print("\n\nMerge back:")
root = merge(L, R)
inorder(root)