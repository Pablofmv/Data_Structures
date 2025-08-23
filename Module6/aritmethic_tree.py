class Node:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0
        self.size = 1

def height(n):
    return n.height if n else -1

def size(n):
    return n.size if n else 0

def update_height(n):
    n.height = 1 + max(height(n.left), height(n.right))
    n.size = 1 + size(n.left) + size(n.right)

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

    x.parent = y.parent
    y.parent = x

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
    
    if balance < 1:
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
    elif key > root.key:
        root.right = insert(root.right, key)
        root.right.parent = root
    else:
        return root
    
    return rebalance(root)

def inorder(n):
    if n:
        inorder(n.left)
        print(f"{n.key}(h={n.height},s={n.size})",end = " ")
        inorder(n.right)

def kth_smallest(R, k):

    if not R or k < 1 or k > size(R):
        raise IndexError("k out of range")
    
    s = size(R.left)

    if k == s + 1:
        return R.key
    elif k <= s:
        return kth_smallest(R.left, k)
    else:
        return kth_smallest(R.right, k - s - 1)
    
def rank(R, key):
    r = 1
    cur = R
    while cur:
        if key <= cur.key:
            cur = cur.left
        else:
            r += size(cur.left) + 1


    
    
    




