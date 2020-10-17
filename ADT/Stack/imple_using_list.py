"""
https://www.openbookproject.net/thinkcs/python/english2e/ch19.html
LIFO (Last In First Out)
D
C
B
A
"""
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def get_stack(self):
        return self.items

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return self.items == []

if __name__ == "__main__":
    s = Stack()
    print(s.is_empty())
    s.push("A")
    s.push("B")
    print(s.get_stack())
    s.push("C")
    print(s.get_stack())
    # elem = s.pop()
    # print("pop element is {0}".format(elem))
    s.push("D")
    print(s.get_stack())
    print(s.is_empty())
    print(s.peek())