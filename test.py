class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Linked_list:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, value):
        node = Node(value, self.head)
        self.head = node

    def insert_at_end(self, value):
        if self.head is None:
            self.head = Node(value, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(value, None)

    def print(self):
        itr = self.head
        while itr:
            print(f"-->{itr.data}", end="")
            itr = itr.next
        print()

    def size(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at_index(self, index, value):
        if index == 0:
            self.insert_at_begining(value)
            return
        if index == self.size() - 1:
            self.insert_at_end(value)
            return
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                node = Node(value, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def remove_at_index(self, index):
        if index == 0:
            self.head = self.head.next
            return
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_after_value(self, data, value):
        itr = self.head
        while itr:
            if data == itr.data:
                node = Node(value, itr.next)
                itr.next = node
                break
            itr = itr.next

    def remove_by_value(self, data):
        if self.head.data == data:
            self.head = self.head.next
            return
        itr = self.head
        while itr and itr.next:
            if data == itr.next.data:
                itr.next = itr.next.next
                break
            itr = itr.next

    def reverse_using_prev(self):
        prev = None
        itr = self.head
        while itr:
            itr.next, prev, itr = prev, itr, itr.next
        self.head = prev

    def reverse_using_stack(self):
        stack = []
        itr = self.head
        while itr:
            stack.append(itr.data)
            itr = itr.next
        self.head = None
        while stack:
            self.insert_at_end(stack.pop())

    def empty(self):
        self.head = None


ll = Linked_list()
print(ll.size())
ll.insert_at_begining(2)
ll.insert_at_begining(4)
ll.insert_at_begining(6)
ll.insert_at_begining(8)
ll.print()
ll.remove_at_index(0)
ll.remove_by_value(2)
ll.print()
ll.insert_after_value(4, 40)
ll.insert_at_index(0, 2)
print("\nREVERSING USING PREV:")
print("original")
ll.print()
ll.reverse_using_prev()
print("Reversed")
ll.print()
ll.empty()
ll.insert_at_begining(2)
ll.insert_at_begining(4)
ll.insert_at_begining(6)
ll.insert_at_begining(8)
print("\nREVERSING USING STACK:")
print("original")
ll.print()
ll.reverse_using_stack()
print("reversed")
ll.print()
