# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    stack = []
    cur = 0
    while cur != -1 or stack:
      while cur != -1:
        stack.append(cur)
        cur = self.left[cur]
      cur = stack.pop()
      self.result.append(self.key[cur])
      cur = self.right[cur]
                
    return self.result

  def preOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    stack = [0]
    while stack:
      u = stack.pop()
      self.result.append(self.key[u])
      if self.right[u] != -1:
         stack.append(self.right[u])
      if self.left[u] != -1:
         stack.append(self.left[u])

    return self.result

  def postOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    s1 = [0]
    s2 = []
    while s1:
      u = s1.pop()
      s2.append(u)
      if self.left[u] != -1:
         s1.append(self.left[u])
      if self.right[u] != -1:
         s1.append(self.right[u])
    while s2:
       self.result.append(self.key[s2.pop()])

    return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
