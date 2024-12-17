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
class PriorityQueue:
    def __init__(self):
        self.front = None

    def enqueue(self, value, priority):
        new_node = Node(value, priority)
        if not self.front or self.front.priority > priority:
            new_node.next = self.front
            self.front = new_node
        else:
            current = self.front
            while current.next and current.next.priority <= priority:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def dequeue(self):
        if not self.front:
            raise IndexError("Dequeue from empty priority queue")
        value = self.front.value
        self.front = self.front.next
        return value

    def peek(self):
        if not self.front:
            raise IndexError("Peek from empty priority queue")
        return self.front.value

    def is_empty(self):
        return self.front is None

    def __len__(self):
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count

    def __repr__(self):
        values = []
        current = self.front
        while current:
            values.append((current.value, current.priority))
            current = current.next
        return " -> ".join(f"{v[0]}(p{v[1]})" for v in values)


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

# Priority Queue
priority_queue = PriorityQueue()
priority_queue.enqueue("A", 2)
priority_queue.enqueue("B", 1)
priority_queue.enqueue("C", 3)
print("PriorityQueue:", priority_queue)
print("Dequeue:", priority_queue.dequeue())
print("After Dequeue:", priority_queue)
print("Peek:", priority_queue.peek())
