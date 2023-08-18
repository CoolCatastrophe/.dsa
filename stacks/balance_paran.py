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

    def size(self):
        return len(self.container)

    def is_empty(self):
        return len(self.container) == 0


def is_matching(ch1, ch2):
    match_dict = {
        "]": "[",
        ")": "(",
        "}": "{",
    }
    return match_dict[ch1] == ch2


def is_balanced(code):
    stack = Stack()
    for ch in code:
        if ch in "[({":
            stack.push(ch)
        if ch in "]})":
            if stack.size() == 0:
                return False
            if not is_matching(ch, stack.pop()):
                return False
    return stack.size() == 0


print(is_balanced("{()}"))
print(is_balanced("{()"))
print(is_balanced("{()]"))
print(is_balanced("{(abcd)}"))
