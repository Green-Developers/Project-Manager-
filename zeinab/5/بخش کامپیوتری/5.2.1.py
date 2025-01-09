# پیاده‌سازی صف ساده با لیست پیوندی
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.front = None  # اشاره‌گر به ابتدای صف
        self.rear = None   # اشاره‌گر به انتهای صف
    
    # افزودن عنصر به صف
    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:  # اگر صف خالی باشد
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node  # افزودن به انتهای صف
            self.rear = new_node       # به‌روزرسانی انتهای صف

    # حذف عنصر از ابتدای صف
    def dequeue(self):
        if self.front is None:  # اگر صف خالی باشد
            print("empty")
            return None
        removed_value = self.front.value  # مقدار عنصر حذف شده
        self.front = self.front.next      # به‌روزرسانی ابتدای صف
        if self.front is None:            # اگر صف خالی شود
            self.rear = None
        return removed_value

    # خالی کردن صف
    def makeNull(self):
        self.front = self.rear = None








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














#ادغام ۲صف مرتب شده به هم
def merge_sorted_queues(q1, q2):
    merged_queue = LinkedListQueue()  # صف جدید برای ادغام
    while not (q1.front is None and q2.front is None):  # تا زمانی که هر دو صف خالی نشوند
        if q1.front is None:  # اگر صف اول خالی باشد
            merged_queue.enqueue(q2.dequeue())
        elif q2.front is None:  # اگر صف دوم خالی باشد
            merged_queue.enqueue(q1.dequeue())
        else:
            # مقایسه عنصر اول صف‌ها و افزودن کوچک‌تر به صف جدید
            if q1.front.value <= q2.front.value:
                merged_queue.enqueue(q1.dequeue())
            else:
                merged_queue.enqueue(q2.dequeue())
    return merged_queue

# آزمایش
q1 = LinkedListQueue()
q1.enqueue(1)
q1.enqueue(3)
q1.enqueue(5)

q2 = LinkedListQueue()
q2.enqueue(2)
q2.enqueue(4)
q2.enqueue(6)

merged = merge_sorted_queues(q1, q2)
print("Merged queue")
while merged.front:
    print(merged.dequeue(), end=" ")  # خروجی: 1 2 3 4 5 6







#بررسی تقارن
def is_symmetric(queue):
    elements = []
    current = queue.front
    while current:  # ذخیره عناصر صف در یک لیست
        elements.append(current.value)
        current = current.next
    return elements == elements[::-1]  # بررسی تقارن

# آزمایش
queue = LinkedListQueue()
queue.enqueue(3)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(2)
queue.enqueue(1)

print("is_symmetric", is_symmetric(queue))  # خروجی: True







#مدیریت لیستی از کار ها بر اساس زمان اجرا
def manage_tasks(tasks):
    task_queue = PriorityQueue()
    for task in tasks:
        name, time = task
        task_queue.enqueue(name, time)  # افزودن کارها به صف

    print("Reversed runtime list")
    executed_tasks = []  # برای ذخیره کارهایی که اجرا شده‌اند
    while not task_queue.empty():
        task = task_queue.dequeue()
        executed_tasks.append(task)  # افزودن کار انجام‌شده به لیست

    for task in executed_tasks:
        print(task)  # چاپ کار انجام‌شده

    print("List of tasks in order of execution time")
    for task in reversed(executed_tasks):
        print(task)  # چاپ کارهای معکوس‌شده
# آزمایش
tasks = [("task1", 3), ("task2", 1), ("task3", 5), ("task4", 2)]
manage_tasks(tasks)

