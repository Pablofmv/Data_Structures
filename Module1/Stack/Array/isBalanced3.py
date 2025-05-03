def IsBalanced(str):

    stack = []

    for char in str:

        if char in ["(","["]:
            stack.append(char)
        else:

            if len(stack) == 0:
                return False
            
            top = stack.pop()

            if (top == '(' and char != ')') and (top == "[" and char != "]"):
                return False
            
    return len(stack) == 0

test_str = "()[]([])"
print(IsBalanced(test_str))