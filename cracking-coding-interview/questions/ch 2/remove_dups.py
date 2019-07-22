# Q2.1 Write code to remove duplicates from a linked list

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

def remove_duplicates(ll):
    root = ll.root
    elems = set([root.data])

    prev = root
    root = prev.child

    while root is not None:
        # If duplicate then remove this link
        if root.data in elems:
            prev.child = root.child
            root = prev.child
            continue

        # Else add to unique list
        elems.add(root.data)
        prev = prev.child
        root = root.child
            
    return ll

ll = LinkedList([1, 7, 9, 7, 3, 76, 6, 1, 1])

print(remove_duplicates(ll))