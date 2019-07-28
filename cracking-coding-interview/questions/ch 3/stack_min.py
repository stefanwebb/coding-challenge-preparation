# Q3.2: How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element? Push, pop, and min should all operate in O(1) time.

class StackMin(object):
    def __init__(self, data=[]):
        assert isinstance(data, list)
        self.data = []
        
        for elem in data:
            self.append(elem)
        
    def append(self, elem):
        # Update min
        if len(self.data) == 0:
            self.min_ = [elem]
            
        else:
            if elem < self.min_[-1]:
                self.min_.append(elem)
            else:
                self.min_.append(self.min_[-1])
        
        self.data.append(elem)
        
    def pop(self):
        self.min_.pop()
        return self.data.pop()
    
    def min(self):
        return self.min_[-1]

stack = StackMin([5, 3, 6, 7, 1])
stack.pop()

"""
Solution notes

Could do a bit better by abbreviating when multiple values are repeated in self.min_

Notes on mistakes I made

1. Again, got some of the logic wrong from what I was thinking. Write down the pseudo-code and have brain fully switched on!

"""