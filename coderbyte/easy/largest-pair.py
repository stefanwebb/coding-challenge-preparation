# Have the function LargestPair(num) take the num parameter being passed and determine the largest double digit number within the whole number. For example: if num is 4759472 then your program should return 94 because that is the largest double digit number. The input will always contain at least two positive digits.

def LargestPair(num): 
    digits = [int(i) for i in list(str(num))]
    maxNum = 0
    
    for idx in range(len(digits)-1):
        num = digits[idx]*10 + digits[idx+1]
        if num > maxNum:
            maxNum = num

    # code goes here 
    return maxNum

print(LargestPair(363223311))