#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  n = len(tree)
  if n == 0:
    return True
  
  key = [t[0] for t in tree]
  left = [t[1] for t in tree]
  right = [t[2] for t in tree]

  stack = []
  cur = 0
  prev = None

  while cur != -1 or stack:
    while cur != -1:
      stack.append(cur)
      cur = left[cur]
    
    cur = stack.pop()

    if prev is not None and key[cur] <= prev:
      return False

    prev = key[cur]
    cur = right[cur] 

  return True


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
