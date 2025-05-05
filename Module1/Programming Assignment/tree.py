def print_tree(node, children, level =0, prefix =""):
    indent = " "*level
    print(f"{indent}{prefix}Node {node}")

    for child in children[node]:
        print_tree(child, children, level +1, prefix="|--")

def compute_height(n, parents):

    children = [[] for _ in range(n)]
    root = -1

    for i in range(0,n):
        parent = parents[i]

        if parent == -1:
            root = i
        else:
            children[parent].append(i)
        
    print("Tree Structure")
    print_tree(root, children)
    print()

def main():
    n = int(input())
    parents = list(map(int,input().split()))

    height = compute_height(n, parents)  # Compute height
    print("Height of the tree:", height)

if __name__ == "__main__":
    main()