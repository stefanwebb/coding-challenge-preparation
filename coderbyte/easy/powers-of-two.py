# Have the function PowersofTwo(num) take the num parameter being passed which will be an integer and return the string true if it's a power of two. If it's not return the string false. For example if the input is 16 then your program should return the string true but if the input is 22 then the output should be the string false. 

def countBits(x):
    if x == 0:
        return 0
    else:
        return (x % 2) + countBits(x//2)

def PowersofTwo(num):
    return countBits(num) == 1