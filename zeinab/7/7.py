class Tree:
    # هر گره شامل فرزند چپ، فرزند راست و داده است
    LC: object = None  # فرزند چپ
    RC: object = None  # فرزند راست
    Data: object = None  # داده گره


class BinaryTree:
    def __init__(self):
        # ایجاد درخت دودویی با یک گره ریشه خالی
        self.root = Tree()
    
    def insert(self, value, node: Tree = None):
        # متد درج یک مقدار در درخت
        if self.root.Data is None:
            # اگر درخت خالی است، مقدار به عنوان ریشه قرار می‌گیرد
            self.root.Data = value
            return
        if node is None:
            # شروع از گره ریشه
            node = self.root
        if value < node.Data:
            # اگر مقدار کمتر از داده گره فعلی باشد، به سمت چپ می‌رود
            if node.LC is None:
                # اگر فرزند چپ وجود ندارد، یک گره جدید ایجاد و مقدار را درج می‌کنیم
                new_node = Tree()
                new_node.Data = value
                node.LC = new_node
            else:
                # اگر فرزند چپ وجود دارد، به صورت بازگشتی به سمت چپ می‌رویم
                self.insert(value, node.LC)
        else:
            # اگر مقدار بزرگ‌تر یا مساوی باشد، به سمت راست می‌رود
            if node.RC is None:
                # اگر فرزند راست وجود ندارد، گره جدید ایجاد و مقدار را درج می‌کنیم
                new_node = Tree()
                new_node.Data = value
                node.RC = new_node
            else:
                # اگر فرزند راست وجود دارد، به صورت بازگشتی به سمت راست می‌رویم
                self.insert(value, node.RC)
        return node
    
    def sizeOfNode(self):
        # محاسبه تعداد گره‌های درخت
        return BinaryTree.SizeOfNode(self.root)

    @staticmethod
    def SizeOfNode(node: Tree):
        # متد بازگشتی برای محاسبه تعداد گره‌ها
        if node is None:
            # اگر گره خالی باشد، مقدار 0 بازگردانده می‌شود
            return 0
        # تعداد گره‌ها = 1 + تعداد گره‌های چپ + تعداد گره‌های راست
        return 1 + BinaryTree.SizeOfNode(node.LC) + BinaryTree.SizeOfNode(node.RC)

    def find_Node(self, node: Tree, value):
        # پیدا کردن یک گره خاص در درخت
        if self.root is None:
            return
        if node is None:
            node = self.root
        if node.LC is not None:
            # جستجو در زیر درخت چپ
            self.find_Node(node.LC, value)
        if node.Data == value:
            # اگر مقدار گره برابر با مقدار جستجو شده باشد، آن گره بازگردانده می‌شود
            return node
        if node.RC is not None:
            # جستجو در زیر درخت راست
            self.find_Node(node.RC, value)
        
    def delete(self, node: Tree, value):
        # حذف یک گره از درخت
        if self.root is None:
            return
        if node is None:
            node = self.root
        if node.LC is not None:
            # حذف از زیر درخت چپ
            self.delete(node.LC, value)
        if node.Data == value:
            # جایگزینی گره با فرزند سمت راست
            node = node.RC
        if node.RC is not None:
            # حذف از زیر درخت راست
            self.delete(node.RC, value)

    def get_height(self):
        # محاسبه ارتفاع درخت
        return BinaryTree.get_height(self.root)

    @staticmethod
    def get_height(node: Tree):
        # متد بازگشتی برای محاسبه ارتفاع درخت
        if node is None:
            return 0
        # ارتفاع = 1 + ماکزیمم ارتفاع چپ و راست
        return 1 + max(BinaryTree.get_height(node.LC), BinaryTree.get_height(node.RC))

    def LMC(self, node=None):
        # پیدا کردن کوچک‌ترین گره در درخت
        if self.root is None:
            return
        if node is None:
            node = self.root
        if node.LC is not None:
            # حرکت به سمت چپ برای پیدا کردن کوچک‌ترین مقدار
            self.LMC(node.LC)
        if node.LC is None and node.RC is None:
            # اگر گره بدون فرزند باشد، بازگردانده می‌شود
            return node
        if node.RC is not None:
            self.LMC(node.RC)

    def parent(self, node: Tree):
        # پیدا کردن والد یک گره
        if self.root is None:
            return "Error"
        self.find_Node(self.root.LC, node)
        if self.root == node:
            # اگر گره برابر با ریشه باشد، والد آن خود ریشه است
            return self.root
        self.find_Node(self.root.RC, node)

    def print_preorder(self, node=None):
        # پیمایش پیش‌ترتیب درخت
        if self.root is None:
            print("Tree is empty")
            return
        if node is None:
            node = self.root
        print(node.Data, end=" ")  # چاپ داده گره
        if node.LC is not None:
            self.print_preorder(node.LC)
        if node.RC is not None:
            self.print_preorder(node.RC)

    def print_inorder(self, node=None):
        # پیمایش در ترتیب درخت
        if self.root is None:
            return
        if node is None:
            node = self.root
        if node.LC is not None:
            self.print_inorder(node.LC)
        print(node.Data, end=" ")  # چاپ داده گره
        if node.RC is not None:
            self.print_inorder(node.RC)

    def print_postorder(self, node=None):
        # پیمایش پس‌ترتیب درخت
        if self.root is None:
            return
        if node is None:
            node = self.root
        if node.LC is not None:
            self.print_postorder(node.LC)
        if node.RC is not None:
            self.print_postorder(node.RC)
        print(node.Data, end=" ")  # چاپ داده گره

    @staticmethod
    def create_tree(inorder: list, postorder: list):
        # ایجاد درخت از روی ترتیب میانی و پس‌ترتیب
        if not inorder or not postorder:
            return None
        root_value = postorder.pop()  # آخرین مقدار پس‌ترتیب به عنوان ریشه انتخاب می‌شود
        root = Tree()
        root.Data = root_value
        root_index = inorder.index(root_value)  # پیدا کردن موقعیت ریشه در ترتیب میانی
        # بازسازی زیر درخت راست و چپ به صورت بازگشتی
        root.RC = BinaryTree.create_tree(inorder[root_index + 1:], postorder)
        root.LC = BinaryTree.create_tree(inorder[:root_index], postorder)
        return root
    


if __name__ == "__main__":
    # Create a binary tree
    bt = BinaryTree()
    bd=BinaryTree()
    values = [10, 15, 3, 7, 12, 18]
    for val in values:
        bd.insert(val)

    # Test 1: Insert values into the tree
    values = [10, 5, 15, 3, 7, 12, 18]
    for val in values:
        bt.insert(val)

    print("Tree after inserting values:")
    print("Pre-order Traversal:")
    bt.print_preorder()
    print("\nIn-order Traversal:")
    bt.print_inorder()
    print("\nPost-order Traversal:")
    bt.print_postorder()



    # Test 3: Count the number of nodes in the tree
    print("Number of nodes in the tree:", bt.sizeOfNode())

    # Test 4: Search for a specific node
    search_value = 8
    result = bt.find_Node(bt.root, search_value)
    if result:
        print(f"Node with value {search_value} found.")
    else:
        print(f"Node with value {search_value} does not exist.")

    # Test 5: Delete a node
    delete_value = 5
    print(f"Deleting node with value {delete_value}.")
    bt.delete(bt.root, delete_value)
    print("Tree after deletion:")
    bd.print_postorder()
    # Test 6: Create a tree from in-order and post-order traversals
    inorder = [3, 5, 7, 10, 12, 15, 18]
    postorder = [3, 7, 5, 12, 18, 15, 10]
    print("\nCreating a tree from in-order and post-order traversals:")
    new_tree = BinaryTree()
    new_tree.root = BinaryTree.create_tree(inorder, postorder)
    print("In-order Traversal of the new tree:")
    new_tree.print_inorder()