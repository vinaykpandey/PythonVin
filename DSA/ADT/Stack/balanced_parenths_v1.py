"""
Use a stack to check whether or not a string
has balanced usage of parenthesis
e.g.:
    1: () 2: ()() 3: (({[]}))  => Balanced
    1: (() 2: {{{)}] 3: [][]]] => Not Balanced

"""
from collections import deque
class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def get_stack(self):
        return self.container

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False

def is_parenths_balanced(par_string):
    s = Stack()
    is_balanced = True
    index = 0
    while index < len(par_string) and is_balanced:
        paren = par_string[index]
        if paren in "({[":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
        index += 1
    if s.is_empty() and is_balanced:
        return True
    else:
        return False

print(is_parenths_balanced("({{}[]})"))
print(is_parenths_balanced("({{}[]]]})"))