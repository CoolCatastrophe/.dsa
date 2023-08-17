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

    def get_length(self):
        if self.head is None:
            return 0
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count += 1
        return count

    def insert_list(self, lst):
        for item in lst:
            self.insert_at_begining(item)

    def insert_at_end(self, value):
        if self.head is None:
            self.insert_at_begining(value)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(value, None)

    def print(self):
        if self.head is None:
            return
        itr = self.head
        while itr:
            print(f"-->{itr.data}", end=" ")
            itr = itr.next
        print()

    def insert_at_index(self, index, value):
        if index < 0 or index > self.get_length():
            return
        if index == 0:
            self.insert_at_begining(value)
        if index == self.get_length() - 1:
            self.insert_at_end(value)
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(value, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def remove_at_index(self, index):
        if index < 0 or index > self.get_length() - 1:
            return
        if index == 0:
            self.head = self.head.next
        itr = self.head
        count = 0
        while itr:
            if index - 1 == count:
                itr.next = itr.next.next
                break
            count += 1
            itr = itr.next

    def insert_after_value(self, data, value):
        itr = self.head
        while itr:
            if itr.data == data:
                node = Node(value, itr.next)
                itr.next = node
                break
            itr = itr.next

    def remove_by_value(self, value):
        if self.head is None:
            return
        if self.head.data == value:
            self.head = self.head.next
        itr = self.head
        while itr and itr.next:
            if itr.next.data == value:
                itr.next = itr.next.next
                break
            itr = itr.next


ll = Linked_list()
ll.insert_list(["banana", "mango", "grapes", "orange"])
ll.print()
ll.insert_after_value("mango", "apple")  # insert apple after mango
ll.print()
ll.remove_by_value("orange")
ll.print()
ll.remove_by_value("banana")
ll.remove_by_value("mango")
ll.remove_by_value("apple")
ll.remove_by_value("grapes")
ll.remove_by_value("orange")
ll.insert_at_end("orange")
ll.print()
