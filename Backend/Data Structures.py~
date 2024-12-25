class Node:
    def __init__(self, value, priority=0):
        self.value = value
        self.priority = priority
        self.next = None

# -------------------------------------------------------------------------------------
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            prev = None
            i = 0
            while current and i < index:
                prev = current
                current = current.next
                i += 1
            if i == index:
                prev.next = new_node
                new_node.next = current
            else:
                raise IndexError("Index out of range")

    def remove(self, value):
        current = self.head
        prev = None
        while current:
            if current.value == value:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return
            prev = current
            current = current.next
        raise ValueError(f"{value} not found in the list")

    def pop(self, index=0):
        if not self.head:
            raise IndexError("Pop from empty list")
        current = self.head
        prev = None
        i = 0
        while current and i < index:
            prev = current
            current = current.next
            i += 1
        if current:
            if prev:
                prev.next = current.next
            else:
                self.head = current.next
            return current.value
        else:
            raise IndexError("Index out of range")

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def __getitem__(self, index):
        current = self.head
        i = 0
        while current:
            if i == index:
                return current.value
            current = current.next
            i += 1
        raise IndexError("Index out of range")

    def __repr__(self):
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return " -> ".join(map(str, values))

# -------------------------------------------------------------------------------------

# Example Usage
# Linked List
linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.insert(1, 15)
print("LinkedList:", linked_list)
linked_list.remove(15)
print("After Remove:", linked_list)
print("Pop:", linked_list.pop())
print("Final List:", linked_list)

