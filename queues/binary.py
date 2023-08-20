from collections import deque
import time


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

    def print_queue(self):
        if not self.is_empty():
            for n in self.buffer:
                print(n, end="")
            print()
        else:
            print("Empty Queue")

    def front(self):
        if not self.is_empty():
            return self.buffer[-1]
        else:
            return None


def generate_binary_numbers(n):
    q = Queue()
    q.enqueue("1")
    print("0")
    for _ in range(n):
        front = q.front()
        print(front)
        q.enqueue(front + "0")
        q.enqueue(front + "1")
        q.dequeue()


t = time.time()
n = 20
if __name__ == "__main__":
    generate_binary_numbers(20)
print(f"Generating {n} Numbers took {time.time()-t} seconds")
