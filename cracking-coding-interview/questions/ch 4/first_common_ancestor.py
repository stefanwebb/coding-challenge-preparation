# Q4.8: First common ancestor

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

# First common ancestor is first node where nodes in question are on left and right side
def first_common_ancestor(root, x, y):
    left = root.children[0]
    right = root.children[1]

    # If no children...
    if left is None and right is None:
        return None

    # If this node is one of x,y...
    elif root.name == x or root.name == y:
        return None

    # If only one child...
    elif left is None or right is None:
        child = left if right is None else right

        # If child is one of the nodes in question then return root
        if child.name == x or child.name == y:
            return root.name

        # Else repeat for child
        return first_common_ancestor(child, x, y)

    else:
        if left.name == x or left.name == y or right.name == x or right.name == y:
            return root.name
        
        # Otherwise, find out which side of root x and y are on
        is_left = []

        def traverse(node):
            left = node.children[0]
            right = node.children[1]

            if node.name == x:
                is_left.append(x)
            elif node.name == y:
                is_left.append(y)
            
            if left is not None:
                traverse(left)
            if right is not None:
                traverse(right)

        traverse(left)

        # If both on same side
        if x in is_left and y in is_left:
            return first_common_ancestor(left, x, y)
        elif (x not in is_left) and (y not in is_left):
            return first_common_ancestor(right, x, y)

        # If on opposite sides then this is the first common ancestor
        else:
            return root.name

print(non_bst)

print(first_common_ancestor(non_bst, '0', '1'))