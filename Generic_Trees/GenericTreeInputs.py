class GenericTreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []


def predefined_generic_tree_inputs():
    # Tree 1
    root1 = GenericTreeNode(1)
    child1 = GenericTreeNode(2)
    child2 = GenericTreeNode(3)
    root1.children.append(child1)
    root1.children.append(child2)

    child1.children.append(GenericTreeNode(4))
    child1.children.append(GenericTreeNode(5))

    # Tree 2
    root2 = GenericTreeNode(10)
    child1 = GenericTreeNode(20)
    child2 = GenericTreeNode(30)
    child3 = GenericTreeNode(40)
    root2.children.append(child1)
    root2.children.append(child2)
    root2.children.append(child3)

    child2.children.append(GenericTreeNode(50))
    child2.children.append(GenericTreeNode(60))

    # Tree 3
    root3 = GenericTreeNode(100)
    child1 = GenericTreeNode(200)
    root3.children.append(child1)
    root3.children.append(GenericTreeNode(300))

    child1.children.append(GenericTreeNode(400))
    child1.children.append(GenericTreeNode(500))

    return root1, root2, root3

