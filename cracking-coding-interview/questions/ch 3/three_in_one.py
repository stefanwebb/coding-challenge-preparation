# Q3.1: Describe how you could use a single array to implement three stacks.

class ThreeStacks(object):
    def __init__(self):
        """
        Empty array of three elements
        """
        self.data = [None]*3
        self.size = [0,0,0]
        
    def push(self, item, stack):
        """
        Push element onto one of the three stacks
        """
        assert stack >= 0 and stack < 3
        
        # Calculate where item would go in array
        idx = self._last(stack)
        
        # Add additional elements if required
        while idx >= len(self.data):
            self.data.append(None)
            
        # Set element
        self.data[idx] = item
        self.size[stack] += 1

    def _idx(self, stack, idx):
        return idx*3 + stack

    def _last(self, stack):
        return self._idx(stack, self.size[stack])
    
    def pop(self, stack):
        """
        Pop and return element from one of the three stacks
        """
        assert stack >= 0 and stack < 3
        
        if not self.size[stack]:
            raise Exception('Popping from empty stack!')
        
        idx = self._idx(stack, self.size[stack]-1)
        self.size[stack] -= 1
        
        if idx == len(self.data) - 1:
            return self.data.pop()
        
        else:
            return self.data[idx]

    def __repr__(self):
        repr = []
        for stack in range(3):
            repr.append('stack: ' +  str(stack) + ' data: ' + ' '.join([str(self.data[self._idx(stack, idx)]) for idx in range(self.size[stack])]))
        return '\n'.join(repr)
        
stack = ThreeStacks()
stack.push(3, 2)
stack.push(9, 0)
stack.push(10, 2)
stack.push(5, 1)

stack.pop(2)

"""
Reflections on solution

1. I forgot some of the logic in the functions! I.e. to increase size in push and decrease in pop. I should write down some comments/pseudo-code in templates so I don't forget this!
2. I almost forgot to use self as first parameter in class methods.
3. I iterated over wrong variable in for loop.
4. I forgot to input all the arguments when calling a method I designed: _idx(...)

"""

print(stack)
