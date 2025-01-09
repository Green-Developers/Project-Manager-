class Node:
    def __init__(self, data):
        # مقدار داده (Data) و اشاره‌گر به گره بعدی (Next)
        self.Data = data
        self.Next = None

class LinkedList:
    def __init__(self):
        # سر لیست یا اولین گره (L)
        self.L = None

    def insert_at_end(self, value):
        # درج یک گره جدید در انتهای لیست
        new_node = Node(value)
        if self.L is None:
            self.L = new_node
        else:
            temp = self.L
            while temp.Next:
                temp = temp.Next
            temp.Next = new_node

    def print_forward(self):
        # چاپ مقادیر لیست به ترتیب
        temp = self.L
        while temp:
            print(temp.Data, end="-")
            temp = temp.Next
        print("None")

    def search_and_count(self, value):
        # جستجو و شمارش تعداد وقوع یک مقدار در لیست
        temp = self.L
        index = 0
        count = 0
        first_position = None
        while temp:
            if temp.Data == value:
                count += 1
                if first_position is None:
                    first_position = index
            temp = temp.Next
            index += 1

        if count > 0:
            return f"Element found at index {first_position} with {count} occurrences."
        else:
            return "Data not found!"

class LinkedListOperations:
    @staticmethod
    def split_even_odd(list):
        # تقسیم لیست پیوندی به دو لیست مجزا: گره‌های با اندیس زوج و فرد
        even_list = LinkedList()
        odd_list = LinkedList()
        temp = list.L
        index = 0
        while temp:
            if index % 2 == 0:
                even_list.insert_at_end(temp.Data)
            else:
                odd_list.insert_at_end(temp.Data)
            temp = temp.Next
            index += 1
        
        print("Even index list:")
        even_list.print_forward()
        print("Odd index list:")
        odd_list.print_forward()

    @staticmethod
    def merge_sorted_lists(list1, list2):
        # ادغام دو لیست پیوندی مرتب‌شده به یک لیست مرتب‌شده جدید
        new_list = LinkedList()
        temp1 = list1.L
        temp2 = list2.L
        while temp1 and temp2:
            if temp1.Data < temp2.Data:
                new_list.insert_at_end(temp1.Data)
                temp1 = temp1.Next
            else:
                new_list.insert_at_end(temp2.Data)
                temp2 = temp2.Next
        
        while temp1:
            new_list.insert_at_end(temp1.Data)
            temp1 = temp1.Next
        
        while temp2:
            new_list.insert_at_end(temp2.Data)
            temp2 = temp2.Next

        return new_list

# تست 1: جستجو و شمارش تعداد وقوع یک عنصر
linked_list = LinkedList()
linked_list.insert_at_end(10)
linked_list.insert_at_end(20)
linked_list.insert_at_end(20)
linked_list.insert_at_end(30)
linked_list.insert_at_end(20)

print("Test 1: Search and Count")
print(linked_list.search_and_count(20))  # خروجی: Element found at index 1 with 3 occurrences.
print(linked_list.search_and_count(10))  # خروجی: Element found at index 0 with 1 occurrences.
print(linked_list.search_and_count(40))  # خروجی: Data not found!

# تست 2: تقسیم لیست به دو لیست زوج و فرد
linked_list2 = LinkedList()
linked_list2.insert_at_end(1)
linked_list2.insert_at_end(2)
linked_list2.insert_at_end(3)
linked_list2.insert_at_end(4)
linked_list2.insert_at_end(5)

print("\nTest 2: Split Even and Odd")
LinkedListOperations.split_even_odd(linked_list2)

# تست 3: ادغام دو لیست پیوندی مرتب‌شده به یک لیست جدید مرتب‌شده
list1 = LinkedList()
list1.insert_at_end(10)
list1.insert_at_end(30)
list1.insert_at_end(50)

list2 = LinkedList()
list2.insert_at_end(20)
list2.insert_at_end(40)
list2.insert_at_end(60)

merged_list = LinkedListOperations.merge_sorted_lists(list1, list2)

print("\nTest 3: Merge Sorted Lists")
merged_list.print_forward()  # خروجی: 10-20-30-40-50-60-None