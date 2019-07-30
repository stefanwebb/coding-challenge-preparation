class Node(object):
    """
    Node structure for a tree
    """
    countNodes = 0

    def __init__(self, data=None, name=None, children=[None, None]):
        self.name = name if name is not None else str(Node.countNodes)
        self.data = data
        self.children = children
        Node.countNodes += 1

    def __repr__(self):
        """
        DFS to print tree nodes/values
        """
        strings = []

        def traverse(depth, node):
            strings.append(' '*2*depth + node.name + ': ' + str(node.data))
            for child in node.children:
                if child is not None:
                    traverse(depth+1, child)

        traverse(0, self)
        return '\n'.join(strings)


# Debug (non-search) binary tree
non_bst = Node(8, children=[Node(4, children=[Node(2), Node(12)]), Node(10, children=[None, Node(20)])])
bst = Node(8, children=[Node(4, children=[Node(2), Node(6)]), Node(10, children=[None, Node(20)])])

print(bst)