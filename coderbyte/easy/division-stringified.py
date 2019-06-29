# Have the function DivisionStringified(num1,num2) take both parameters being passed, divide num1 by num2, and return the result as a string with properly formatted commas. If an answer is only 3 digits long, return the number with no commas (ie. 2 / 3 should output "1"). For example: if num1 is 123456789 and num2 is 10000 the output should be "12,346". 

def DivisionStringified(num1,num2):
    ansStr = str(int(round(float(num1) / num2)))
    
    # Add in commas
    numCommas = (len(ansStr)-1)//2
    parts = []
    idx = len(ansStr)
    for idx in range(len(ansStr)-3, 0, -3):
        parts.append(ansStr[idx:(idx+3)])
    
    parts.append(ansStr[0:idx])
    ans = ','.join(reversed(parts))

    # code goes here 
    return ans
    
# keep this function call here  
print DivisionStringified(raw_input())