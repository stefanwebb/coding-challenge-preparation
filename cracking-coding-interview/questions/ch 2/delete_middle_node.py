# Q2.3 Implement an algorithm to delete a node in the middle (i.e. not but the first and last, not necessarily the exact middle) of a singly linked list, given only access to that node.

class LinkedList(object):
    def __init__(self, data=[]):
        self.root = None

        for item in data:
            if self.root is None:
                self.root = LinkedNode(item, None)
                thisNode = self.root
            else:
                newNode = LinkedNode(item, None)
                thisNode.child = newNode
                thisNode = newNode
    
    def __str__(self):
        items = []
        thisNode = self.root

        while thisNode is not None:
            items.append(str(thisNode.data))
            thisNode = thisNode.child

        return ', '.join(items)

class LinkedNode(object):
    def __init__(self, data, child):
        self.data = data
        self.child = child

def delete_middle_node(ll, node):
    prev = ll.root
    if prev is None:
        return ll
    root = prev.child

    while root.child is not None:
        if root.data == node:
            prev.child = root.child
            break

        prev = prev.child
        root = root.child

    return ll

ll = LinkedList([1, 7, 9, 3, 6, 1.5])

print(delete_middle_node(ll, 7))