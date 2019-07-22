# Q2.4 Write code to partition a linked list around a value x such that all nodes less than x come before all nodes greater than or equal to x. (Important: The partition element x can appear anywhere in the right partition, it does not need to appear between the left and right partitions.)

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

def partition(ll, node):
    leftRoot = None
    leftThis = None
    leftPrev = None

    thisNode = ll.root
    prevNode = None

    # Break off the nodes one at a time and add to left/right partitions
    while thisNode:
        # If data is less than value, break off and add to left parition
        if thisNode.data < node:
            # If this node is root, then advance the root of the right partition
            if thisNode is ll.root:
                ll.root = thisNode.child

            # Otherwise remove connection to previous node
            else:
                prevNode.child = thisNode.child

            # If no left root yet then set it
            if leftRoot is None:
                leftRoot = thisNode
                leftThis = leftRoot

            # Otherwise
            else:
                leftThis.child = thisNode
                leftThis = leftThis.child

            thisNode = leftThis.child
            leftThis.child = None

        else:
            prevNode = thisNode
            thisNode = thisNode.child

    # Combine left and right partitions
    if leftRoot is not None:
        leftThis.child = ll.root
        ll.root = leftRoot

    return ll

#ll = LinkedList([3, 5, 8, 5, 10, 2, 1, 7])
ll = LinkedList([6, 7, 9, 10, 5])

print(partition(ll, 5))