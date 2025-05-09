# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []

    for i, next in enumerate(text):
        if next in "([{])]}":
            if next in "([{":
                # Process opening bracket, write your code here
                opening_brackets_stack.append((next,i))
            elif next in ")]}":
                # Process closing bracket, write your code here
                if len(opening_brackets_stack) == 0:
                    return i + 1
                
                pop_char, pop_pos = opening_brackets_stack.pop()

                if (pop_char == "(" and next != ")") or (pop_char == "[" and next != "]") or (pop_char == "{" and next != "}"):
                    return i + 1
    
    if opening_brackets_stack:
        _, pos = opening_brackets_stack[0]
        return pos + 1
            
    return "Success" if len(opening_brackets_stack) == 0 else i + 1


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
