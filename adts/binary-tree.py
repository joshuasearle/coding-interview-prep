class BinaryTreeNode(object):
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
    
    def __eq__(self, other):
        return self.value == other.value
    
    def __lt__(self, other):
        return self.value < other.value
    
    def __gt__(self, other):
        return self.value > other.value


class BinaryTree(object):
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        self.root = self.insert_aux(value, self.root)

    @staticmethod
    def insert_aux(value, current):
        if current is None:
            current = BinaryTreeNode(value)
        elif current.value > value:
            current.left = BinaryTree.insert_aux(value, current.left)
        elif current.value < value:
            current.right = BinaryTree.insert_aux(value, current.right)
        return current
    
    def __contains__(self, value):
        return BinaryTree.contains_aux(self.root, value)

    @staticmethod
    def contains_aux(current, value):
        if current is None:
            return False
        elif current.value > value:
            return BinaryTree.contains_aux(current.left, value)
        elif current.value < value:
            return BinaryTree.contains_aux(current.right, value)
        else:
            return True
    
    def inorder_traversal(self):
        order = []
        BinaryTree.inorder_traversal_aux(self.root, order)
        return order

    @staticmethod
    def inorder_traversal_aux(current, order):
        if current is None: return
        BinaryTree.inorder_traversal_aux(current.left, order)
        order.append(current.value)
        BinaryTree.inorder_traversal_aux(current.right, order)
    
    def preorder_traversal(self):
        order = []
        BinaryTree.preorder_traversal_aux(self.root, order)
        return order

    @staticmethod
    def preorder_traversal_aux(current, order):
        if current is None: return
        order.append(current.value)
        BinaryTree.preorder_traversal_aux(current.left, order)
        BinaryTree.preorder_traversal_aux(current.right, order)

    def postorder_traversal(self):
        order = []
        BinaryTree.postorder_traversal_aux(self.root, order)
        return order

    @staticmethod
    def postorder_traversal_aux(current, order):
        if current is None: return
        BinaryTree.postorder_traversal_aux(current.left, order)
        BinaryTree.postorder_traversal_aux(current.right, order)
        order.append(current.value)

        

b = BinaryTree()
print(b.root)
b.insert(3)
b.insert(2)
b.insert(1)
b.insert(4)
print(b.inorder_traversal())
print(b.preorder_traversal())
print(b.postorder_traversal())