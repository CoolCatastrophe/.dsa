# We can use deque to implement stack
from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, value):
        return self.container.append(value)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


str = '"We will conquere Covid - 19"'
stck = Stack()
for s in str:
    stck.push(s)

while not stck.is_empty():
    print(f"{stck.pop()}", end="")
print()

code = """))((a+b}{(("""

stack = Stack()

for i in code:
    stack.push(i)

count = 0

while not stack.is_empty():
    ele = stack.pop()
    if ele == "{" or ele == "(" or ele == "[":
        count += 1
    if ele == "}" or ele == ")" or ele == "]":
        count -= 1

if count == 0:
    print("Balanced")
else:
    print("Not Balanced")
