# Have the function BinaryReversal(str) take the str parameter being passed, which will be a positive integer, take its binary representation (padded to the nearest N * 8 bits), reverse that string of bits, and then finally return the new reversed string in decimal form. For example: if str is "47" then the binary version of this integer is 101111 but we pad it to be 00101111. Your program should reverse this binary string which then becomes: 11110100 and then finally return the decimal version of this string, which is 244.

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

def BinaryReversal(s):
    binaryStr = writeBinaryString(int(s))
    
    excess = len(binaryStr) % 8
    padding = 0 if excess == 0 else 8 - excess
    
    binaryStr = '0'*padding + binaryStr
    ans = str(readBinaryString(''.join(list(reversed(binaryStr)))))

    # code goes here 
    return ans

BinaryReversal("4567")