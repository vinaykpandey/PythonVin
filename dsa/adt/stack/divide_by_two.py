"""
Use a stack data structure to convert integer values
to binary
e.g.: 242

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

def div_by_2(dec_num):
    s = Stack()
    while dec_num > 0:
        r = dec_num % 2
        s.push(r)
        dec_num = dec_num // 2

    bin_num = ""
    while not s.is_empty():
        bin_num += str(s.pop())

    return bin_num

print(div_by_2(242))