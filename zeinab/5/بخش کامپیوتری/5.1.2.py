# پیاده‌سازی صف اولویت
class PriorityNode:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.head = None  # اشاره‌گر به ابتدای صف

    # افزودن عنصر به صف با توجه به اولویت
    def enqueue(self, value, priority):
        new_node = PriorityNode(value, priority)
        if self.head is None or self.head.priority < priority:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.priority >= priority:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    # حذف عنصر با بالاترین اولویت
    def dequeue(self):
        if self.head is None:
            print("صف خالی است!")
            return None
        removed_value = self.head.value
        self.head = self.head.next
        return removed_value

    # تعداد عناصر صف
    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    # بررسی خالی بودن صف
    def empty(self):
        return self.head is None

    # بازگرداندن مقدار با بالاترین اولویت
    def peek(self):
        if self.head is None:
            print("صف خالی است!")
            return None
        return self.head.value

    # خالی کردن صف
    def makeNull(self):
        self.head = None

# آزمایش صف اولویت
p_queue = PriorityQueue()
p_queue.enqueue("کار1", 3)
p_queue.enqueue("کار2", 5)
p_queue.enqueue("کار3", 2)
print("عنصر با بالاترین اولویت:", p_queue.dequeue())  # کار2
print("اندازه صف:", p_queue.size())  # 2
print("آیا صف خالی است؟", p_queue.empty())  # False
p_queue.makeNull()
print("پس از خالی کردن:", p_queue.empty())  # True