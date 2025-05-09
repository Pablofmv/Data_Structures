
def print_tree(node, children, level = 0, prefix = ""):

    indent = " " * level
    print(f"{indent} {prefix} Node {node}")

    for child in children[node]:
        print_tree(child, children, level + 1, prefix = "|--")

def compute_height(n, parents):

    children = [[] for i in range(0,n)]
    root = 0

    for i in range(0,n):

        parent = parents[i]

        if parent == -1:
            root = i
        else:
            children[parent].append(i)
    
    print(children)
    print("Print tree:")
    print_tree(root, children)

    def dfs(node):

        if not children[node]:
            return 1
        
        tallest_height_child = 0
        
        for child in children[node]:

            height_child = dfs(child)
            tallest_height_child = max(height_child, tallest_height_child)
        
        return tallest_height_child + 1
    
    return dfs(root)


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    height = compute_height(n, parents)
    print(height)

if __name__ == "__main__":
    main()