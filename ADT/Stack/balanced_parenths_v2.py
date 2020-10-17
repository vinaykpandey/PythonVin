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

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

def is_match(ch1, ch2):
    match_dict = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    return match_dict[ch1] == ch2

def is_balanced(string):
    stack = Stack()
    for ch in string:
        if ch in "({[":
            stack.push(ch)
        elif ch in ")}]":
            if stack.size() == 0:
                return False
            elif not is_match(ch, stack.pop()):
                return False
    return stack.size()==0

if __name__ == '__main__':
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("((a+g))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))


