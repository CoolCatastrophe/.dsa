from collections import deque


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, data):
        self.buffer.appendleft(data)

    def dequeue(self):
        self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

    def print(self):
        if not self.is_empty():
            for n in self.buffer:
                print(n,end="")
            print()
        else:
            print("Empty Queue")

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.print()
q.dequeue()
q.print()
q.dequeue()
q.print()
q.dequeue()
q.print()
q.dequeue()
q.print()
q.dequeue()
q.print()