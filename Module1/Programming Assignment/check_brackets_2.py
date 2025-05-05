# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{]})":

            if next in "([{":
                opening_brackets_stack.append((i,next))
                pass

            if next in ")]}":
                # Process closing bracket, write your code here
                if len(opening_brackets_stack) == 0:
                    return i + 1
                
                pop_i, pop_next = opening_brackets_stack.pop()

                if (pop_next == "(" and next !=  ")") or (pop_next == "[" and next !=  "]") or (pop_next == "{" and next !=  "}"):
                    return i + 1
    
    if opening_brackets_stack:
        pos, char = opening_brackets_stack[0]
        return pos + 1
    
    return "Success"


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
