# Have the function ABCheck(str) take the str parameter being passed and return the string true if the characters a and b are separated by exactly 3 places anywhere in the string at least once (ie. "lane borrowed" would result in true because there is exactly three characters between a and b). Otherwise return the string false. 

# NOTE: Didn't read question carefully! 'b' can follow 'a' by 3 characters also.

def ABCheck(str):
    for i in range(len(str)-4):
        char = str[i]
        
        if (char == 'a' and str[i+4] == 'b') or (char == 'b' and str[i+4] == 'a'):
            return 'true'

    # code goes here 
    return 'false'

# TODO: Version with regular expressions!
    
# keep this function call here  
print(ABCheck(raw_input()))