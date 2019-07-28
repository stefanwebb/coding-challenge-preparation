# Q3.4: Implement a MyQueue class which implements a queue using two stacks

class MyQueue(object):
    def __init__(self, data=[]):
        self.queue = data

    def append(self, elem):
        self.queue.append(elem)

    def dequeue(self):
        assert len(self.queue) > 1

        temp = []
        while len(self.queue) > 1:
            temp.append(self.queue.pop())
        ans = self.queue.pop()

        while len(temp) > 0:
            self.queue.append(temp.pop())

        return ans

    def __repr__(self):
        return self.queue.__repr__()

queue = MyQueue([2, 3, 7, 8, 8, 3])
print(queue)
print(queue.dequeue())
print(queue)

"""
Reflections on solution

Don't press F5 or Ctrl+F5 in CoderPad!!! This will reset the window.

There is a slightly better solution, where we don't do pushing/popping for every dequeue.
Instead you maintain stackNewest and stackOldest...

"""