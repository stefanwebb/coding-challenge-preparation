# Have the function BitwiseOne(strArr) take the array of strings stored in strArr, which will only contain two strings of equal length that represent binary numbers, and return a final binary string that performed the bitwise OR operation on both strings. A bitwise OR operation places a 0 in the new string where there are zeroes in both binary strings, otherwise it places a 1 in that spot. For example: if strArr is ["1001", "0100"] then your program should return the string "1101" 

def readBinaryString(s):
    number = 0
    mask = 1
    for i in range(len(s)):
        if s[-i-1] == '1':
            number |= mask
        mask <<= 1
    return number
    
def writeBinaryString(x):
    if x <= 0:
        return '0'

    digits = []
    mask = 1
    
    while x > 0:
        if x & 1:
            digits.append('1')
        else:
            digits.append('0')
        x >>= 1
    
    return ''.join(reversed(digits))
        

def BitwiseOne(strArr):
    x, y = [readBinaryString(s) for s in strArr]
    
    unpadded = writeBinaryString(x | y)
    
    padStr = '0'*(len(strArr[0])-len(unpadded))

    # code goes here
    return padStr+unpadded