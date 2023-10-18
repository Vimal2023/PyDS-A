class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def _height(self, node):
        if not node:
            return 0
        return node.height

    def _balance(self, node):
        if not node:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _update_height(self, node):
        if not node:
            return
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _rotate_right(self, y):
        x = y.left
        T = x.right

        x.right = y
        y.left = T

        self._update_height(y)
        self._update_height(x)

        return x

    def _rotate_left(self, x):
        y = x.right
        T = y.left

        y.left = x
        x.right = T

        self._update_height(x)
        self._update_height(y)

        return y

    def _balance_node(self, node):
        balance = self._balance(node)

        if balance > 1:
            if self._balance(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1:
            if self._balance(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def insert(self, root, key):
        if not root:
            return AVLNode(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root

        self._update_height(root)
        return self._balance_node(root)

    def delete(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp

            temp = self._find_min(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        self._update_height(root)
        return self._balance_node(root)

    def _find_min(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def inorder_traversal(self, root):
        result = []
        if root:
            result = self.inorder_traversal(root.left)
            result.append(root.key)
            result += self.inorder_traversal(root.right)
        return result

# Example usage
if __name__ == "__main__":
    avl_tree = AVLTree()
    root = None

    keys = [9, 5, 10, 0, 6, 11, -1, 1, 2]
    for key in keys:
        root = avl_tree.insert(root, key)

    print("Inorder traversal of the constructed AVL tree is:")
    print(avl_tree.inorder_traversal(root))

    root = avl_tree.delete(root, 10)

    print("Inorder traversal after deletion of 10:")
    print(avl_tree.inorder_traversal(root))
