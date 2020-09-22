"""
https://www.openbookproject.net/thinkcs/python/english2e/ch19.html
"""

class Stack:
    def __init__(self):
        self.items = []
    def push(self, items):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return (self.items == [])