# Q4.6: Successor
class Node(object):
    """
    Node structure for a tree
    """
    countNodes = 0

    def __init__(self, data=None, name=None, children=[None, None]):
        self.parent = None
        self.name = name if name is not None else str(Node.countNodes)
        self.data = data
        self.children = children

        for c in self.children:
            if c is not None:
                c.parent = self

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

def successor(node):
    parent = node.parent
    right = node.children[1]

    # Take right node if we can...
    if right is not None:
        ans = right
        # ...then keep branching left
        while ans.children[0] is not None:
            ans = ans.children[0]

        return ans

    # Otherwise...
    else:
        #...find first parent that is greater than current value
        while parent is not None:
            if parent.data >= node.data:
                return parent
            parent = parent.parent
        return None

    return ans

node = bst.children[0].children[0]
while node is not None:
    print(node.data)
    node = successor(node)