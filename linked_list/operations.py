class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Linked_list:
    def __init__(self):
        self.head = None

    def at_begining(self, value):
        node = Node(value, self.head)
        self.head = node

    def at_end(self, value):
        if self.head is None:
            self.head = Node(value, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(value, None)

    def insert_list(self, lt):
        self.head = None
        for item in lt:
            self.at_begining(item)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            print("Invalid Index")
            return

        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, value):
        if index < 0 or index >= self.get_length():
            print("Invalid Index")
            return
        if index == 0:
            self.at_begining(value)
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(value, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def print(self):
        if self.head is None:
            print("Empty Linked List :( ")
            return
        itr = self.head
        while itr:
            print(f"-->{itr.data}", end="")
            itr = itr.next
        print()


if __name__ == "__main__":
    linked_list = Linked_list()
    linked_list.at_begining(3)
    linked_list.at_begining(4)
    linked_list.at_begining(5)
    linked_list.print()
    linked_list.insert_list(["a", "b", "c", "d"])
    linked_list.print()
    print(linked_list.get_length())
    linked_list.remove_at(2)
    linked_list.print()
    print(linked_list.get_length())
    linked_list.insert_at(1, "z")
    linked_list.print()
    linked_list.remove_at(0)
    linked_list.print()
    print(linked_list.get_length())
