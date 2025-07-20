class Node:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
    
def find(k, root):

    if root is None:
        return None
    if root.key == k:
        return root
    elif k < root.key:
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

    while N.parent and N == N.parent.right:
        N = N.parent
    return N.parent

def connect(parent, child, is_left = True):

    if is_left:
        parent.left = child
    else:
        parent.right = child
    if child:
        child.parent = parent


root = Node(7)
n4 = Node(4)
n13 = Node(13)
n1 = Node(1)
n6 = Node(6)
n10 = Node(10)
n15 = Node(15)

connect(root, n4, True)
connect(root, n13, False)
connect(n4, n1, True)
connect(n4, n6, False)
connect(n13, n10, True)
connect(n13, n15, False)
c

target = find(6, root)
print(target.key)

succ = next_node(target)
print(succ.key)

