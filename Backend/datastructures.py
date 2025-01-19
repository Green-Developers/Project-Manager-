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
class QueueNode:
    def __init__(self, value, priority):
        self.value = value 
        self.priority = priority
        self.next = None 

class PriorityQueue:
    def __init__(self):
        self.front = None 

    def enqueue(self, task):
        priority = task.end_date
        new_node = QueueNode(task, priority)

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
        task = self.front.value
        self.front = self.front.next
        return task

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
            task = current.value
            values.append(f"{task.name}(end: {task.end_date})")
            current = current.next
        return " -> ".join(values)

# --------------------------------------------------------------------------------------
class Stack:
    def __init__(self, capacity=None):
        self.top = None
        self.capacity = capacity
        self.current_size = 0

    def push(self, item):
        if self.capacity and self.current_size >= self.capacity:
            raise OverflowError("Stack is full.")
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self.current_size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack.")
        popped_data = self.top.data
        self.top = self.top.next
        self.current_size -= 1
        return popped_data

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty stack.")
        return self.top.data

    def empty(self):
        self.top = None
        self.current_size = 0

    def is_empty(self):
        return self.top is None

    def is_full(self):
        if self.capacity is None:
            return False
        return self.current_size >= self.capacity

    def size(self):
        return self.current_size

    def reverse(self):
        prev = None
        current = self.top
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.top = prev
# --------------------------------------------------------------------------------------
class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("Queue is full")

        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        item = self.queue[self.front]
        self.queue[self.front] = None

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity

        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue[self.front]

    def size(self):
        if self.is_empty():
            return 0
        if self.rear >= self.front:
            return self.rear - self.front + 1
        return self.capacity - self.front + self.rear + 1

    def __str__(self):
        if self.is_empty():
            return "Queue is empty"
        if self.rear >= self.front:
            return " -> ".join(map(str, self.queue[self.front: self.rear + 1]))
        return " -> ".join(map(str, self.queue[self.front:] + self.queue[: self.rear + 1]))

# --------------------------------------------------------------------------------------
class MinHeap:
    def __init__(self):
        self.heap = []

    def _parent(self, index: int) -> int:
        return (index - 1) // 2

    def _left_child(self, index: int) -> int:
        return 2 * index + 1

    def _right_child(self, index: int) -> int:
        return 2 * index + 2

    def _swap(self, index1: int, index2: int):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def _heapify_up(self, index: int):
        while index > 0 and self.heap[self._parent(index)].name > self.heap[index].name:
            self._swap(self._parent(index), index)
            index = self._parent(index)

    def _heapify_down(self, index: int):
        smallest = index
        left = self._left_child(index)
        right = self._right_child(index)

        if left < len(self.heap) and self.heap[left].name < self.heap[smallest].name:
            smallest = left
        if right < len(self.heap) and self.heap[right].name < self.heap[smallest].name:
            smallest = right
        if smallest != index:
            self._swap(index, smallest)
            self._heapify_down(smallest)

    def insert(self, item):
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if len(self.heap) == 0:
            raise IndexError("extract_min from empty heap")
        self._swap(0, len(self.heap) - 1)
        min_item = self.heap.pop()
        self._heapify_down(0)
        return min_item

    def build_heap(self, items):
        self.heap = items
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._heapify_down(i)

    def sorted(self):
        sorted_list = []
        while len(self.heap) > 0:
            sorted_list.append(self.extract_min())
        return sorted_list

# --------------------------------------------------------------------------------------
class TaskHashMap:
    def __init__(self):
        self.map = {}

    def put(self, key, value):
        self.map[key.id] = value

    def get(self, key):
        return self.map.get(key.id, None)

    def remove(self, key):
        if key.id in self.map:
            del self.map[key.id]

    def contains(self, key):
        return key.id in self.map

    def size(self):
        return len(self.map)

    def clear(self):
        self.map.clear()

    def all_items(self):
        return self.map.items()
