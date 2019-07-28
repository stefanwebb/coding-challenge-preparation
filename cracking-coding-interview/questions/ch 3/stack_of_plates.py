# Q3.3: Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed several stacks and should create a new stack once the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack (that is, pop() should return the same values as it woudl if there were just a single stack).

class StackOfPlates(object):
    def __init__(self, threshold=10):
        assert threshold > 0
        
        self.stacks = [[]]
        self.threshold = threshold
        
    def push(self, elem):
        # Work out whether to create new stack
        if len(self.stacks[-1]) == self.threshold:
            self.stacks.append([])
        
        # Put element into last stack
        self.stacks[-1].append(elem)
    
    def pop(self):
        # Remove last element
        ans = self.stacks[-1].pop()
        
        # Remove last stack if empty
        if len(self.stacks[-1]) == 0:
            self.stacks.pop()
        
        return ans
    
    def __repr__(self):
        return ', '.join([s.__repr__()[1:-1] for s in self.stacks])
    
stack = StackOfPlates(3)

for x in [1, 2, 3, 4]:
    stack.push(x)
stack.pop()

print(stack)
