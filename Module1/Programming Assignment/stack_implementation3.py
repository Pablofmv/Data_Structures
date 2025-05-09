q = int(input())

stack = []
max_stack = []

for i in range(0,q):

    query = list(input().split())

    if query[0] == "push":
        value = query[1]
        stack.append(value)

        if not max_stack or value > max_stack[-1]:
            max_stack.append(value)
        else:
            max_stack.append(max_stack[-1])
    
    elif query[0] == "pop":

        if not max_stack:
            continue
        
        stack.pop()
        max_stack.pop()
    
    elif query[0] == "max":

        if not max_stack:
            continue

        print(max_stack[-1])


