# Have the function ProductDigits(num) take the num parameter being passed which will be a positive integer, and determine the least amount of digits you need to multiply to produce it. For example: if num is 24 then you can multiply 8 by 3 which produces 24, so your program should return 2 because there is a total of only 2 digits that are needed. Another example: if num is 90, you can multiply 10 * 9, so in this case your program should output 3 because you cannot reach 90 without using a total of 3 digits in your multiplication. 

import math

def ProductDigits(num):
    # Upper bound is number * 1
    minLen = len(str(num))+1
    
    # Loop through all products of two numbers
    # Why does only considering x*y suffice?
    for idx in range(2, int(math.ceil(math.sqrt(num)))):
        if num % idx == 0:
            thisLen = len(str(idx)) + len(str(num // idx))
            if thisLen < minLen:
                minLen = thisLen

    # code goes here 
    return minLen

print(ProductDigits(48))