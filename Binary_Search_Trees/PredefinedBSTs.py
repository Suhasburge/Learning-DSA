class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def print_bst(root):
    if root is None:
        return

    print_bst(root.left)
    print(root.data, end=" ")
    print_bst(root.right)


def create_predefined_bsts_manual():
    # Tree-1
    root1 = BinaryTreeNode(10)
    root1.left = BinaryTreeNode(5)
    root1.right = BinaryTreeNode(15)

    # Tree-2
    root2 = BinaryTreeNode(20)
    root2.left = BinaryTreeNode(10)
    root2.right = BinaryTreeNode(30)
    root2.left.left = BinaryTreeNode(5)
    root2.left.right = BinaryTreeNode(15)
    root2.right.left = BinaryTreeNode(25)
    root2.right.right = BinaryTreeNode(35)

    # Tree-3
    root3 = BinaryTreeNode(40)
    root3.left = BinaryTreeNode(20)
    root3.right = BinaryTreeNode(60)
    root3.left.left = BinaryTreeNode(10)
    root3.left.right = BinaryTreeNode(30)
    root3.left.left.left = BinaryTreeNode(5)
    root3.left.left.right = BinaryTreeNode(15)
    root3.left.right.left = BinaryTreeNode(25)
    root3.left.right.right = BinaryTreeNode(35)
    root3.right.left = BinaryTreeNode(50)
    root3.right.right = BinaryTreeNode(70)
    root3.right.left.right = BinaryTreeNode(55)
    root3.right.right.left = BinaryTreeNode(65)
    root3.right.right.right = BinaryTreeNode(75)

    return root1, root2, root3


root1, root2, root3 = create_predefined_bsts_manual()
