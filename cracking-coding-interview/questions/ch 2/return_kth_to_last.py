# Q2.2 Implement an algorithm to find the kth to last element of a singly linked list.

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

# Solution 1: Method using double-ended queue => deque
# Run-time is O(N) and memory is O(k), where N is length of list.
def return_kth_last(root, k):
    assert k > 0

    elems = []
    while root is not None:
        # Remove from queue/stack if necessary
        if len(elems) == k:
            elems = elems[1:]

        # Add to queue and navigate to next element
        elems.append(root.data)
        root = root.child

    if len(elems) == k:
        return elems[0]
    else:
        return None

# Solution 1.5: Method using built-in deque
# Run-time is O(N) and memory is O(k), where N is length of list.
from collections import deque
def return_kth_last2(root, k):
    assert k > 0

    elems = deque([])
    while root is not None:
        # Remove from queue/stack if necessary
        if len(elems) == k:
            elems.popleft()

        # Add to queue and navigate to next element
        elems.append(root.data)
        root = root.child

    if len(elems) == k:
        return elems.popleft()
    else:
        return None

"""
Notes on solution:

1. Start with naive solution and improve upon it.
2. Give code a once over after writing solution looking for bugs.
3. Think of edge cases!
4. Describe time/memory complexity.

"""

# TODO: Review singly and doubly linked lists

# Solution 2: Method that memory scales as O(1). Use two pointers!
def return_kth_last3(root, k):
    assert k > 0

    ans = root
    count = 0

    while root is not None:
        if count >= k:
            ans = ans.child

        root = root.child
        count += 1

    if count >= k:
        return ans.data
    else:
        return None

ll = LinkedList([1, 7, 9, 3, 6])
#print(return_kth_last(ll.root, 1))
#print(return_kth_last2(ll.root, 3))
print(return_kth_last3(ll.root, 1))

# It works!