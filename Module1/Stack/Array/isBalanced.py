def IsBalanced(str):

    stack = []
    for char in str:
        if char in ['(','[']:
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            
            top = stack.pop()

            if (top == '[' and char != ']') or (top == '(' and char != ')'):
                return False
    
    return len(stack) == 0

test_string = "([()][])"
print(IsBalanced(test_string))
