# Q 3.6

# Q 3.6

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
    
    def __repr__(self):
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

class AnimalShelter(object):
    def __init__(self):
        self.ll = LinkedList()
        
    def __repr__(self):
        return self.ll.__repr__()

    def enqueue(self, name, isdog=True):
        if self.ll.root is None:
            self.ll.root = LinkedNode((name, isdog), None)
        
        else:
            temp = self.ll.root
            self.ll.root = LinkedNode((name, isdog), temp)
            
    
    def dequeueAny(self):
        ans = self.ll.root.data
        self.ll.root = self.ll.root.child
        return ans
    
    def dequeueDog(self):
        thisNode = self.ll.root
        prevNode = None
        
        while not thisNode.data[1]:
            if thisNode.child is None:
                raise Exception('No dogs in queue')
            else:
                prevNode = thisNode
                thisNode = thisNode.child
                
        ans = thisNode.data
                
        if prevNode is None:
            self.ll.root = thisNode.child
            
        else:
            prevNode.child = thisNode.child
                            
        return ans
    
    def dequeueCat(self):
        thisNode = self.ll.root
        prevNode = None
        
        while thisNode.data[1]:
            if thisNode.child is None:
                raise Exception('No cats in queue')
            else:
                prevNode = thisNode
                thisNode = thisNode.child
                
        ans = thisNode.data
                
        if prevNode is None:
            self.ll.root = thisNode.child
            
        else:
            prevNode.child = thisNode.child
                            
        return ans

shelter = AnimalShelter()
shelter.enqueue('Rupert')
shelter.enqueue('Felix', isdog=False)
shelter.enqueue('Milo')
elem = shelter.dequeueCat()
print(shelter, elem)

"""
Notes on solution

There is a better solution, where we maintain two queues, one for dogs, one for cats, and use a timestamp to determine which is dequeueAny from.

"""