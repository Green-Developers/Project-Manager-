# کلاس گره برای لیست پیوندی
class Node:
    def __init__(self, data):
        # مقدار داده (Data) و اشاره‌گر به گره بعدی (Next)
        self.Data = data
        self.Next = None

    def dispose(self):
        # پاک کردن داده و اشاره‌گرها
        self.Data = None
        self.Next = None


# کلاس گره برای لیست پیوندی دوطرفه
class DoubleNode:
    def __init__(self, data):
        # مقدار داده (Data)، اشاره‌گر به گره بعدی (Next) و قبلی (Prev)
        self.Data = data
        self.Next = None
        self.Prev = None

    def dispose(self):
        # پاک کردن داده و اشاره‌گرها
        self.Data = None
        self.Next = None
        self.Prev = None


# کلاس لیست پیوندی
class LinkedList:
    def __init__(self):
        # سر لیست یا اولین گره (L)
        self.L = None

    def insert_at_front(self, value):
        # درج یک گره جدید در ابتدای لیست
        new_node = Node(value)
        new_node.Next = self.L  # گره جدید به گره قبلی لینک می‌شود
        self.L = new_node  # گره جدید به عنوان سر لیست قرار می‌گیرد

    def insert_at_end(self, value):
        # درج یک گره جدید در انتهای لیست
        new_node = Node(value)
        if self.L is None:  # اگر لیست خالی باشد
            self.L = new_node
        else:
            temp = self.L
            # پیمایش تا آخرین گره
            while temp.Next:
                temp = temp.Next
            temp.Next = new_node  # لینک گره آخر به گره جدید

    def is_empty(self):
        # بررسی خالی بودن لیست
        return self.L is None

    def search(self, value):
        # جستجوی یک مقدار در لیست
        temp = self.L
        while temp:
            if temp.Data == value:  # اگر مقدار پیدا شد
                return temp.Data
            temp = temp.Next
        return "Data not found!"  # اگر مقدار پیدا نشد

    def clear(self):
        # پاک کردن کل لیست
        temp = self.L
        while temp:
            next_node = temp.Next  # نگهداری گره بعدی
            temp.dispose()  # پاک کردن داده گره فعلی
            temp = next_node
        self.L = None  # سر لیست را خالی می‌کنیم

    def size(self):
        # محاسبه تعداد گره‌ها
        temp = self.L
        size = 0
        while temp:
            size += 1
            temp = temp.Next
        return size

    def delete_at_front(self):
        # حذف گره اول لیست
        if self.is_empty():  # اگر لیست خالی باشد، خطا می‌دهد
            raise ValueError("LinkedList is empty!")
        temp = self.L
        self.L = self.L.Next  # سر لیست به گره بعدی تغییر می‌کند
        temp.dispose()

    def print_forward(self):
        # چاپ مقادیر لیست به ترتیب
        temp = self.L
        while temp:
            print(temp.Data, end="-")
            temp = temp.Next
        print("None")

    def reverse_recursive(self, current=None, prev=None):
        # معکوس کردن لیست به صورت بازگشتی
        if current is None:  
            current = self.L
        if current.Next is None:  # رسیدن به انتهای لیست
            self.L = current  # گره آخر به عنوان سر لیست قرار می‌گیرد
            current.Next = prev
            return
        next_node = current.Next
        current.Next = prev
        self.reverse_recursive(next_node, current)

    def reverse_non_recursive(self):
        # معکوس کردن لیست به صورت غیر بازگشتی
        prev = None
        current = self.L
        while current:
            next_node = current.Next  # نگهداری گره بعدی
            current.Next = prev  # معکوس کردن لینک‌ها
            prev = current
            current = next_node
        self.L = prev  # گره آخر به عنوان سر لیست قرار می‌گیرد

    def make_double(self):
        # تبدیل لیست پیوندی به لیست پیوندی دوطرفه
        if self.is_empty():
            raise ValueError("LinkedList is empty!")

        double_head = DoubleNode(self.L.Data)  # تبدیل سر لیست
        temp = self.L.Next
        current_double = double_head

        while temp:
            temp_double = DoubleNode(temp.Data)  # ایجاد گره دوطرفه جدید
            current_double.Next = temp_double
            temp_double.Prev = current_double
            current_double = temp_double
            temp = temp.Next

        return double_head

    def make_circular(self):
        # تبدیل لیست به لیست پیوندی حلقوی
        if self.is_empty():
            raise ValueError("LinkedList is empty!")
        temp = self.L
        while temp.Next:
            temp = temp.Next
        temp.Next = self.L  # گره آخر به سر لیست لینک می‌شود


class DoubleLinkedList:
    def __init__(self):
        # سر لیست پیوندی دوطرفه
        self.L = None

    def insert_at_end(self, value):
        # درج گره در انتهای لیست دوطرفه
        new_node = DoubleNode(value)
        if self.L is None:
            self.L = new_node
        else:
            temp = self.L
            while temp.Next:
                temp = temp.Next
            temp.Next = new_node
            new_node.Prev = temp

    def delete_at_end(self):
        # حذف گره آخر لیست دوطرفه
        if self.L is None:
            raise ValueError("DoubleLinkedList is empty!")
        temp = self.L
        if temp.Next is None:  # اگر فقط یک گره وجود داشته باشد
            self.L = None
            return
        while temp.Next:
            temp = temp.Next
        temp.Prev.Next = None  # لینک گره دوم به آخر را خالی می‌کنیم
        temp.dispose()

    def backward_print(self):
        # چاپ مقادیر لیست به صورت معکوس
        if self.L is None:
            print("empty")
            return
        temp = self.L
        while temp.Next:  # پیمایش تا آخرین گره
            temp = temp.Next
        while temp:
            print(temp.Data, end="_")
            temp = temp.Prev  # حرکت به سمت گره قبلی















            # ایجاد یک لیست پیوندی
linked_list = LinkedList()

# تست درج در ابتدای لیست
linked_list.insert_at_front(10)
linked_list.insert_at_front(20)
linked_list.insert_at_front(30)
linked_list.print_forward()  # خروجی باید: 30-20-10-None

# تست درج در انتهای لیست
linked_list.insert_at_end(40)
linked_list.insert_at_end(50)
linked_list.print_forward()  # خروجی باید: 30-20-10-40-50-None

# تست جستجو
print(linked_list.search(20))  # خروجی باید: <Node object with value 20>
print(linked_list.search(60))  # خروجی باید: Data not found!

# تست خالی بودن لیست
print(linked_list.is_empty())  # خروجی باید: False

# تست پاک کردن کل لیست
linked_list.clear()
linked_list.print_forward()  # خروجی باید: None
print(linked_list.is_empty())  # خروجی باید: True

# تست اندازه لیست
linked_list.insert_at_front(10)
linked_list.insert_at_end(20)
linked_list.insert_at_end(30)
print(linked_list.size())  # خروجی باید: 3

# تست












