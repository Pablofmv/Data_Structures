# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []

    for i, next in enumerate(text):
        counter += 1
        if next in "([{])]}":
            if next in "([{":
                # Process opening bracket, write your code here
                opening_brackets_stack.append(next)

            if next in ")]}":
                # Process closing bracket, write your code here
                if len(opening_brackets_stack) == 0:
                    return i + 1
                
                pop = opening_brackets_stack.pop()

                if (pop == "(" and next != ")") or (pop == "[" and next != "]") or (pop == "{" and next != "}"):
                    return i + 1
            
    return "Success" if len(opening_brackets_stack) == 0 else counter


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
