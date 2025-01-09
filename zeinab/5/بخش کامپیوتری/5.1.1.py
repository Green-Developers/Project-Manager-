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

# آزمایش صف ساده
queue = LinkedListQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("deleted item", queue.dequeue())  
queue.makeNull()
print("After emptying", queue.dequeue())  








