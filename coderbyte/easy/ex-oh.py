# Have the function ExOh(str) take the str parameter being passed and return the string true if there is an equal number of x's and o's, otherwise return the string false. Only these two letters will be entered in the string, no punctuation or numbers. For example: if str is "xooxxxxooxo" then the output should return false because there are 6 x's and 5 o's. 

def ExOh(str): 
    numX = 0
    
    if len(str) % 2 == 1:
        return 'false'
    
    for c in str:
        if c == 'x':
            numX += 1

    # code goes here 
    return 'true' if numX == len(str) // 2 else 'false'
    
# keep this function call here  
print(ExOh(raw_input()))