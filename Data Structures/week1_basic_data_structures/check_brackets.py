# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, c in enumerate(text):
        if c in "([{":
            opening_brackets_stack.append(Bracket(c, i))
            pass

        if c in ")]}":
            if are_matching(opening_brackets_stack[-1].char, c):
                opening_brackets_stack.pop(-1)
                pass
            else:
                return i + 1           
    return "Success"    

def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)

if __name__ == "__main__":
    main()
