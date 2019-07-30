# Q4.5: Validate BST
from functools import partial

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

def naive_validate_bst(root):
    """
    This solution has O(N^2) runtime, and uses O(N) space
    """
    left = root.children[0]
    right = root.children[1]
    valid_left = valid_right = True

    if left is not None:
        valid_left = max_tree(left) <= root.data and naive_validate_bst(left)

    if right is not None:
        valid_right = min_tree(right) > root.data and naive_validate_bst(right)

    return valid_left and valid_right

def reduce_tree(root, f=min):
    ans = root.data

    for child in root.children:
        if child is not None:
            ans = f(ans, reduce_tree(child, f))

    return ans

max_tree = partial(reduce_tree, f=max)
min_tree = partial(reduce_tree, f=min)

def validate_bst(root):
    """
    Checks if binary tree is a search tree
    BST have property that left descendants <= n, right descendants > n
    """
    
    def traverse(node, f=min):
        ans = True
        left = node.children[0]
        right = node.children[1]
        #node.min = node.data
        #node.max = node.data
        node.val = node.data

        if left is not None:
            ans = traverse(left, f=max) and ans and left.val <= node.data
            
            #node.min = min(node.min, left.min)
            #node.max = max(node.max, left.max)
            node.val = f(node.val, left.val)

        if right is not None:
            ans = traverse(right, f=min) and ans and right.val > node.data

            #node.min = min(node.min, right.min)
            #node.max = max(node.max, right.max)
            node.val = f(node.val, right.val)

        return ans

    return traverse(root)

#print(min_tree(bst))

#print(naive_validate_bst(non_bst))
print(validate_bst(non_bst))