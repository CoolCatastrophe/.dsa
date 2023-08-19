from collections import deque
import time
import threading


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, data):
        return self.buffer.appendleft(data)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

    def print(self):
        for o in self.buffer():
            print(o, end="")
        print


q = Queue()


def place_order(orders):
    for order in orders:
        q.enqueue(order)
        print(f"{order.capitalize()} order taken...")
        time.sleep(0.5)


def serve_order():
    count = 1
    while not q.is_empty():
        o = q.dequeue()
        print(f"order-{count}: {o.capitalize()} Served...")
        time.sleep(1)
        count += 1


orders = ["pizza", "samosa", "pasta", "biryani", "burger"]
t = time.time()
t1 = threading.Thread(target=place_order, args=(orders,))
t2 = threading.Thread(target=serve_order)

t1.start()
t2.start()

t1.join()
t2.join()

print("Done in ", time.time() - t, " seconds")
