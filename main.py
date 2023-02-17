# python3
# Krists Kristaps Dūda 221RDB518
from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next,i))
            
        if next in ")]}":
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) ==0:
                return i+1
            closing = opening_brackets_stack.pop()
            if not are_matching(closing.char, next):
                return i+1
            
    if len(opening_brackets_stack)>0:
        return opening_brackets_stack[0].position +1
    return "Success"


def main():
    input_type = input()
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here]
    if(mismatch)!=None:
        print(mismatch)
    else:
        print("Success")

if __name__ in "__main__":
    main()

