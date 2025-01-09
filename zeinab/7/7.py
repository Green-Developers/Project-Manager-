class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursively(self.root, value)

    def _insert_recursively(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert_recursively(current.left, value)
        else:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert_recursively(current.right, value)

    def find_node(self, value):
        return self._find_node_recursively(self.root, value)

    def _find_node_recursively(self, current, value):
        if current is None or current.value == value:
            return current
        if value < current.value:
            return self._find_node_recursively(current.left, value)
        return self._find_node_recursively(current.right, value)

    def delete(self, value):
        self.root = self._delete_recursively(self.root, value)

    def _delete_recursively(self, current, value):
        if current is None:
            return current

        if value < current.value:
            current.left = self._delete_recursively(current.left, value)
        elif value > current.value:
            current.right = self._delete_recursively(current.right, value)
        else:
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left

            temp = self._find_min(current.right)
            current.value = temp.value
            current.right = self._delete_recursively(current.right, temp.value)

        return current

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def get_height(self):
        return self._get_height_recursively(self.root)

    def _get_height_recursively(self, node):
        if node is None:
            return 0
        left_height = self._get_height_recursively(node.left)
        right_height = self._get_height_recursively(node.right)
        return max(left_height, right_height) + 1

    def get_size(self):
        return self._get_size_recursively(self.root)

    def _get_size_recursively(self, node):
        if node is None:
            return 0
        return 1 + self._get_size_recursively(node.left) + self._get_size_recursively(node.right)

    def inorder_traversal(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.value)
            self.inorder_traversal(node.right, result)
        return result

    def LMC(self):
        if self.root is None:
            return None
        return self._find_min(self.root).value

    def parent(self, node_value):
        return self._find_parent(self.root, node_value, None)

    def _find_parent(self, current, value, parent):
        if current is None:
            return None
        if current.value == value:
            return parent
        if value < current.value:
            return self._find_parent(current.left, value, current)
        return self._find_parent(current.right, value, current)

    def print_preorder(self):
        result = []
        self._preorder_traversal(self.root, result)
        print("Preorder Traversal:", result)

    def _preorder_traversal(self, node, result):
        if node:
            result.append(node.value)
            self._preorder_traversal(node.left, result)
            self._preorder_traversal(node.right, result)

    def print_inorder(self):
        result = []
        self._inorder_traversal(self.root, result)
        print("Inorder Traversal:", result)

    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.value)
            self._inorder_traversal(node.right, result)

    def print_postorder(self):
        result = []
        self._postorder_traversal(self.root, result)
        print("Postorder Traversal:", result)

    def _postorder_traversal(self, node, result):
        if node:
            self._postorder_traversal(node.left, result)
            self._postorder_traversal(node.right, result)
            result.append(node.value)

    def create_tree(self, inorder, postorder):
        if not inorder or not postorder:
            return None
        root_value = postorder.pop()
        root = Node(root_value)
        inorder_index = inorder.index(root_value)
        root.right = self.create_tree(inorder[inorder_index + 1:], postorder)
        root.left = self.create_tree(inorder[:inorder_index], postorder)
        return root

# Example usage
tree = BinaryTree()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(7)

tree.print_inorder()
tree.print_preorder()
tree.print_postorder()
print("Find Node 7:", tree.find_node(7) is not None)
print("Tree Height:", tree.get_height())
print("Tree Size:", tree.get_size())
print("Least Minimum Child (LMC):", tree.LMC())
parent_node = tree.parent(7)
print("Parent of 7:", parent_node.value if parent_node else None)

# Reconstruct a tree from inorder and postorder traversals
inorder_seq = [3, 5, 7, 10, 15]
postorder_seq = [3, 7, 5, 15, 10]
tree.root = tree.create_tree(inorder_seq, postorder_seq)
tree.print_inorder()
tree.print_preorder()
tree.print_postorder()
