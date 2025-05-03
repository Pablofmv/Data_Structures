
def IsBalanced(str):

    stack = []
    for char in str:

        if char in ['(','[']:
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            
            pop = stack.pop()

            if (pop == '(' and char != ')') or (pop == '[' and char != ']'):
                return False
    
    return len(stack) == 0

test = '([])'
print(IsBalanced(test))