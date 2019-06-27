# Have the function LetterCapitalize(str) take the str parameter being passed and capitalize the first letter of each word. Words will be separated by only one space. 

def LetterCapitalize(str):    
    words = [w.capitalize() for w in str.split(' ')]

    # code goes here 
    return " ".join(words)

# TODO: Version that doesn't make use of Python functions
    
# keep this function call here  
print(LetterCapitalize(raw_input()))