
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
    print("")
    print_tree(root, children)

    def dfs(node):

        if not children[node]:
            return 1
        
        tallest_child_height = 0

        for child in children[node]:

            child_height = dfs(child)
            tallest_child_height = max(tallest_child_height, child_height)
        
        return 1 + tallest_child_height
    
    return dfs(root)


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    height = compute_height(n, parents)
    print(height)

if __name__ == "__main__":
    main()