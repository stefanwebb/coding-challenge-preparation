# Q3.5: Write a program to sort a stack such that the smallest items are on the top. You can use an additional stack, but you may not copuy the elements into any other data structure (such as an array). The stack supports the following operations: push, pop, peek, and isEmpty.

def sort_stack(stack):
    temp = []

    # Move the minimum element to the beginning of the stack
    # I.e. a form of insertion sort!
    n = 0
    while n < len(stack):
        # Minimum from elements that haven't been inserted
        min_elem = min(stack[n:])
        
        # Reverse stack elements, removing minimum elements
        count_elem = 0
        while len(stack) > n:
            elem = stack.pop()
            if elem != min_elem:
                temp.append(elem)
            else:
                count_elem += 1
        
        # Put minimum elements at next position in stack
        for _ in range(count_elem):
            stack.append(min_elem)
        
        # Replace reversed elements on stack
        while len(temp) > 0:
            stack.append(temp.pop())
            
        n += count_elem

    return stack

stack = [1, 7, 3, 4, 9, 8, 6, 2, 4]
print(sort_stack(stack))