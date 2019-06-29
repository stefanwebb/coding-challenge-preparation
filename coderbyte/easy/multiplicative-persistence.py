# Have the function MultiplicativePersistence(num) take the num parameter being passed which will always be a positive integer and return its multiplicative persistence which is the number of times you must multiply the digits in num until you reach a single digit. For example: if num is 39 then your program should return 3 because 3 * 9 = 27 then 2 * 7 = 14 and finally 1 * 4 = 4 and you stop at 4.

import operator
import functools

def MultiplicativePersistence(num): 
    ans = 0
    numbers = [int(x) for x in list(str(num))]
    
    while len(numbers) > 1:
        total = functools.reduce(operator.mul, numbers, 1)
        numbers = [int(x) for x in list(str(total))]
        ans += 1

    return ans