# Have the function LongestWord(sen) take the sen parameter being passed and return the largest word in the string. If there are two or more words that are the same length, return the first word from the string with that length. Ignore punctuation and assume sen will not be empty. 

import string

def LongestWord(sen):
    longestWord = []
    thisWord = []
    for char in sen:
        # Skip noncharacters
        if char not in string.punctuation or char.isspace():
            if len(thisWord) > len(longestWord):
                longestWord = thisWord
            thisWord = []
            continue
        
        # Add to current candidate
        thisWord.append(char)
        
    # Check at end of string
    if len(thisWord) > len(longestWord):
        longestWord = thisWord

    # code goes here 
    str = ""
    return str.join(longestWord)
    
# keep this function call here  
print(LongestWord(raw_input()))