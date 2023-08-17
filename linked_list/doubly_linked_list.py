class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class Doubly_linked_list:
    def __init__(self):
        self.head = None

    def print_forward(self):
        itr = self.head
        while itr:
            print(f"-->{itr.data}", end="")
            itr = itr.next
        print()

    def insert_at_begining(self, value):
        node = Node(value, self.head, None)
        if self.head:
            self.head.prev = node
        self.head = node

    def insert_values(self, lst):
        self.head = None
        for data in lst:
            self.insert_at_end(data)

    def insert_at_end(self, value):
        if self.head is None:
            self.head = Node(value, None, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(value, None, itr)

    def insert_at(self, index, value):
        if index==0:
            self.insert_at_begining(value)
            return
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                node = Node(value, itr.next, itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break
            itr = itr.next
            count += 1

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count += 1
        return count

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

    def print_backward(self):
        itr = self.get_last_node()
        while itr:
            print(f"-->{itr.data}", end="")
            itr = itr.prev
        print()

    def remove_at_index(self, index):
        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                if itr.next:
                    itr.next.prev = itr
                break
            count += 1
            itr = itr.next

if __name__ == '__main__':
    ll = Doubly_linked_list()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print_forward()
    ll.print_backward()
    ll.insert_at_end("figs")
    ll.print_forward()
    ll.insert_at(0, "jackfruit")
    ll.print_forward()
    ll.insert_at(6, "dates")
    ll.print_forward()
    ll.insert_at(2, "kiwi")
    ll.print_forward()
