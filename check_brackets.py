# python3

from collections import namedtuple
from array import *

Bracket = namedtuple("Bracket", ["char", "position"])

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text):
    opening_brackets_stack = []
    non_matching_index = 0
    for i, next in enumerate(text):
        if next in "([{":
            B = Bracket(next,i)
            opening_brackets_stack.append(B)
            # Process opening bracket, write your code here
            pass

        if next in ")]}":
            # Process closing bracket, write your code here
            if opening_brackets_stack :
                popped_element = opening_brackets_stack.pop()
                if are_matching(popped_element.char, next):
                    continue
            else : 
                pass
            
            non_matching_index = i+1
            break
    
    if opening_brackets_stack :
        popped_element = opening_brackets_stack.pop()
        non_matching_index = popped_element.position+1
    return non_matching_index


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    if mismatch == 0 :
        print("Success")
    else :
        print(mismatch)

if __name__ == "__main__":
    main()
