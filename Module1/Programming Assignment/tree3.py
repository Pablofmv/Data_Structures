
def print_tree(node, children, level = 0, prefix = ""):

    incidente = " " * level
    print(f"{incidente}{prefix} Node {node}")

    for child in children[node]:
        print_tree(child, children, level + 1, prefix = "|--")

def compute_heights(n, parents):

    children =  [[] for i in range(0,n)]
    root = 0

    for i in range(0,n):
        parent = parents[i]
        
        if parent == -1:
            root = i
        else:
            children[parent].append(i)
    
    print(children)
    print("Tree Structure")
    print_tree(root, children)
    print()


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_heights(n,parents))

if __name__ == "__main__":
    main()