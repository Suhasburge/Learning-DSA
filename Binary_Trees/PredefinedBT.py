class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
from collections import deque

def print_level_wise(root):
    if root is None:
        return
    
    queue = deque([root])

    while queue:
        current_node = queue.popleft()
        print(f"{current_node.data}: ",end = " ")

        if current_node.left:
            print(f"L->{current_node.left.data}",end = ", ")
            queue.append(current_node.left)
        else:
            print("L->None",end = ", ")

        if current_node.right:
            print(f"R->{current_node.right.data}")
            queue.append(current_node.right)
        else:
            print("R->None")

def predefined_binary_tree_inputs():
    # Tree 1: Simple (Height = 3)
    root1 = BinaryTreeNode(1)
    root1.left = BinaryTreeNode(2)
    root1.right = BinaryTreeNode(3)
    root1.left.left = BinaryTreeNode(4)
    root1.left.right = BinaryTreeNode(5)
    root1.right.right = BinaryTreeNode(6)

    # Tree 2: Slightly Complex (Height = 4)
    root2 = BinaryTreeNode(10)
    root2.left = BinaryTreeNode(20)
    root2.right = BinaryTreeNode(30)
    root2.left.left = BinaryTreeNode(40)
    root2.left.right = BinaryTreeNode(50)
    root2.right.left = BinaryTreeNode(60)
    root2.right.right = BinaryTreeNode(70)
    root2.left.left.left = BinaryTreeNode(80)

    # Tree 3: More Complex (Height = 5)
    root3 = BinaryTreeNode(100)
    root3.left = BinaryTreeNode(200)
    root3.right = BinaryTreeNode(300)
    root3.left.left = BinaryTreeNode(400)
    root3.left.right = BinaryTreeNode(500)
    root3.right.left = BinaryTreeNode(600)
    root3.right.right = BinaryTreeNode(700)
    root3.left.left.left = BinaryTreeNode(800)
    root3.left.left.right = BinaryTreeNode(900)
    root3.right.right.left = BinaryTreeNode(1000)
    root3.right.right.right = BinaryTreeNode(1100)

    return root1, root2, root3


# Example usage
root1, root2, root3 = predefined_binary_tree_inputs()
