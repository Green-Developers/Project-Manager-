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
        self.value = value  # مقدار (مثلاً یک شیء تسک)
        self.priority = priority  # اولویت (مثلاً end_date)
        self.next = None  # اشاره‌گر به گره بعدی

class PriorityQueue:
    def __init__(self):
        self.front = None  # گره اول صف

    def enqueue(self, task):
        """
        اضافه کردن تسک به صف بر اساس اولویت (end_date نزدیک‌تر بالاترین اولویت را دارد)
        """
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
        """
        حذف و بازگشت به بالاترین اولویت
        """
        if not self.front:
            raise IndexError("Dequeue from empty priority queue")
        task = self.front.value
        self.front = self.front.next
        return task

    def peek(self):
        """
        مشاهده بالاترین اولویت بدون حذف
        """
        if not self.front:
            raise IndexError("Peek from empty priority queue")
        return self.front.value

    def is_empty(self):
        """
        بررسی خالی بودن صف
        """
        return self.front is None

    def __len__(self):
        """
        شمارش تعداد تسک‌ها در صف
        """
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count

    def __repr__(self):
        """
        نمایش صف به صورت رشته برای بررسی
        """
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
