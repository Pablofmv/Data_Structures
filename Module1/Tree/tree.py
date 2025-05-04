class Node:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def height(self, tree):
        if tree is None:
            return 0
        return 1 +max(self.height(tree.left),self.height(tree.right))
    
    def size(self, tree):
        if tree is None:
            return 0
        return 1 + self.size(tree.left) + self.size(tree.right)
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print(root.height(root))
print(root.size(root)) 