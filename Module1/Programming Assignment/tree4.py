
def print_tree(node, childrens, level = 0, prefix = ""):
    incident = " " * level
    print(f"{incident}{prefix} Node {node}")
    for child in childrens[node]:
        print_tree(child, childrens, level + 1, prefix = "|--")


def calculate_height(n, parents):

    childrens = [[] for i in range(0,n)]
    root = -1

    for i in range(0,n):
        parent = parents[i]

        if parent == -1:
            root = i
        else:
            childrens[parents[i]].append(i)
    
    print(childrens)
    print("Print Tree")
    print_tree(root, childrens)


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    tree = calculate_height(n, parents)

if __name__ == "__main__":
    main()