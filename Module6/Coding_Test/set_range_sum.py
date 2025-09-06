# python3

from sys import stdin

# Splay tree implementation

# Vertex of a splay tree
class Vertex:
  def __init__(self, key, sum, left, right, parent):
    (self.key, self.sum, self.left, self.right, self.parent) = (key, sum, left, right, parent)

def update(v):
  if v is None:
    return
  v.sum = v.key + (v.left.sum if v.left is not None else 0) + (v.right.sum if v.right is not None else 0)
  if v.left is not None:
    v.left.parent = v
  if v.right is not None:
    v.right.parent = v

def smallRotation(v):
  parent = v.parent
  if parent is None:
    return
  grandparent = parent.parent
  if parent.left == v:
    m = v.right
    v.right = parent
    parent.left = m
  else:
    m = v.left
    v.left = parent
    parent.right = m
  update(parent)
  update(v)
  v.parent = grandparent
  if grandparent is not None:
    if grandparent.left == parent:
      grandparent.left = v
    else:
      grandparent.right = v

def bigRotation(v):
  if v.parent.left == v and v.parent.parent.left == v.parent:
    # zig-zig
    smallRotation(v.parent)
    smallRotation(v)
  elif v.parent.right == v and v.parent.parent.right == v.parent:
    # zig-zig
    smallRotation(v.parent)
    smallRotation(v)
  else:
    # zig-zag
    smallRotation(v)
    smallRotation(v)

def splay(v):
  if v is None:
    return None
  while v.parent is not None:
    if v.parent.parent is None:
      smallRotation(v)
      break
    bigRotation(v)
  return v

# find returns (next>=key, new_root)
def find(root, key):
  v = root
  last = root
  nxt = None
  while v is not None:
    if v.key >= key and (nxt is None or v.key < nxt.key):
      nxt = v
    last = v
    if v.key == key:
      break
    if v.key < key:
      v = v.right
    else:
      v = v.left
  root = splay(last)
  return (nxt, root)

def split(root, key):
  (result, root) = find(root, key)
  if result is None:
    return (root, None)
  right = splay(result)
  left = right.left
  right.left = None
  if left is not None:
    left.parent = None
  update(left)
  update(right)
  return (left, right)

def merge(left, right):
  if left is None:
    return right
  if right is None:
    return left
  # move to min of right and splay it to root
  while right.left is not None:
    right = right.left
  right = splay(right)
  right.left = left
  update(right)
  return right

# Code that uses splay tree to solve the problem
root = None

def insert(x):
  global root
  (left, right) = split(root, x)
  new_vertex = None
  if right is None or right.key != x:
    new_vertex = Vertex(x, x, None, None, None)
  root = merge(merge(left, new_vertex), right)

def erase(x):
  global root
  # split at x -> (<x, >=x), then split >=x at x+1 -> ([x], >x)
  left, right = split(root, x)
  mid, right = split(right, x + 1)
  # drop mid (node with key x if it exists)
  root = merge(left, right)

def search(x):
  global root
  nxt, root = find(root, x)   # splay the last accessed node
  return nxt is not None and nxt.key == x

def sum(fr, to):
  global root
  left, middle = split(root, fr)
  middle, right = split(middle, to + 1)
  ans = 0
  if middle is not None:
    ans = middle.sum
  # restore tree
  root = merge(merge(left, middle), right)
  return ans

MODULO = 1000000001
n = int(stdin.readline())
last_sum_result = 0
for _ in range(n):
  line = stdin.readline().split()
  if line[0] == '+':
    x = int(line[1])
    insert((x + last_sum_result) % MODULO)
  elif line[0] == '-':
    x = int(line[1])
    erase((x + last_sum_result) % MODULO)
  elif line[0] == '?':
    x = int(line[1])
    print('Found' if search((x + last_sum_result) % MODULO) else 'Not found')
  elif line[0] == 's':
    l = int(line[1])
    r = int(line[2])
    res = sum((l + last_sum_result) % MODULO, (r + last_sum_result) % MODULO)
    print(res)
    last_sum_result = res % MODULO
