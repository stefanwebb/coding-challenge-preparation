# Have the function DashInsert(str) insert dashes ('-') between each two odd numbers in str. For example: if str is 454793 the output should be 4547-9-3. Don't count zero as an odd number. 

def isOdd(x):
    return x != 0 and x % 2 == 1

def DashInsert(s):
    digits = [int(x) for x in list(s)]
    strings = []
    
    for i in range(len(digits)-1):
        x, y = digits[i], digits[i+1]
        strings.append(str(x))
        if isOdd(x) and isOdd(y):
            strings.append('-')
    strings.append(str(digits[-1]))

    # code goes here 
    return ''.join(strings)