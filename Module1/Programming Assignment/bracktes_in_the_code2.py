def isBalanced(str):

    stack = []
    counter = 0

    for char in str:

        if char in ["[","]","{","}","(",")"]:

            if char in ["[","{","("]:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return counter + 1
            
                pop = stack.pop()

                if (pop == "(" and char != ")") or (pop == "[" and char != "]") or (pop == "{" and char != "}"):
                    return counter + 1
        counter += 1

    return "Success" if len(stack) == 0 else counter

test = "foo(bar[i)"
print(isBalanced(test))