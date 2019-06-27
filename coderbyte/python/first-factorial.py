# Have the function FirstFactorial(num) take the num parameter being passed and return the factorial of it. For example: if num = 4, then your program should return (4 * 3 * 2 * 1) = 24. For the test cases, the range will be between 1 and 18 and the input will always be an integer. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.

def FirstFactorial(num): 
    ans = 1
    
    for i in range(2, num+1):
        ans *= i

    # code goes here 
    return ans

# TODO: A recursive version!
    
# keep this function call here  
print(FirstFactorial(raw_input()))