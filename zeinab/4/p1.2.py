# کلاس گره (Node) برای لیست پیوندی
class Node:
    def __init__(self, data):
        self.Data = data
        self.Next = None


# کلاس لیست پیوندی دایره‌ای
class CircularLinkedList:
    def __init__(self):
        # اشاره‌گر به سر لیست
        self.L = None

    def is_empty(self):
        # بررسی خالی بودن لیست
        return self.L is None

    def insert_at_end(self, value):
        # تابع درج عنصر جدید در انتهای لیست
        new_node = Node(value)
        if self.L is None:  # اگر لیست خالی است
            self.L = new_node
            self.L.Next = self.L  # اشاره به خودش برای دایره‌ای شدن
        else:
            temp = self.L
            while temp.Next != self.L:  # پیمایش تا گره آخر
                temp = temp.Next
            temp.Next = new_node  # لینک گره آخر به گره جدید
            new_node.Next = self.L  # گره جدید به سر لیست لینک می‌شود

    def print_list(self):
        # چاپ عناصر لیست
        if self.is_empty():
            print("List is empty!")
            return
        temp = self.L
        while True:
            print(temp.Data, end=" -> ")
            temp = temp.Next
            if temp == self.L:  # وقتی دوباره به سر لیست برسیم، متوقف می‌شویم
                break
        print("(back to start)")

    def insert_at_start(self, value):
        # تابع درج عنصر جدید در ابتدای لیست
        new_node = Node(value)
        if self.is_empty():
            self.L = new_node
            self.L.Next = self.L
        else:
            new_node.Next = self.L
            temp = self.L
            while temp.Next != self.L:
                temp = temp.Next
            temp.Next = new_node
            self.L = new_node  # سر لیست به گره جدید تغییر می‌کند

# ایجاد یک لیست پیوندی دایره‌ای
cll = CircularLinkedList()

# درج عناصر در انتهای لیست
cll.insert_at_end(10)
cll.insert_at_end(20)
cll.insert_at_end(30)

# چاپ لیست
print("Circular Linked List:")
cll.print_list()

# درج عنصر در ابتدای لیست
cll.insert_at_start(5)
print("\nAfter inserting 5 at the start:")
cll.print_list()