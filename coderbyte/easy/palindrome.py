# Have the function Palindrome(str) take the str parameter being passed and return the string true if the parameter is a palindrome, (the string is the same forward as it is backward) otherwise return the string false. For example: "racecar" is also "racecar" backwards. Punctuation and numbers will not be part of the string. 

# NOTE: This question is a bit ambiguous because whitespace is skipped over

def stripWhitespace(str):
    return ''.join([s if not s.isspace() else '' for s in str.split(' ')])

def Palindrome(str):
    str = stripWhitespace(str)
    
    for i in range(len(str) // 2):
        if str[i] != str[len(str) - i - 1]:
            return 'false'

    # code goes here 
    return 'true'
    
# keep this function call here  
print(Palindrome(raw_input()))