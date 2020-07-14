"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
"""

"""
Counters not a solution as they don't maintain state
Works only if all brackets are of same type

to maintain state, use Stacks
for a expression to be valid, its sub expression shoud also be valid


create a stack
push opening brackets on stack
if the closing bracket is same type as bracket on top, pop and continue
else error

if stack is empty
Valid
"""


def valid_parentheses(expr):

    stk = []

    mapping = {")":"(", "]":"[", "}":"{"}

    for char in expr:
        if char in mapping:
            top_element = stk.pop() if stk else "#"

            if mapping[char] != top_element:
                return False
        else:
            stk.append(char)

    return not stk


expr = "()(())"
print (valid_parentheses(expr))

