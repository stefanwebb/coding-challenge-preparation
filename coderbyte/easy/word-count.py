# Have the function WordCount(str) take the str string parameter being passed and return the number of words the string contains (e.g. "Never eat shredded wheat or cake" would return 6). Words will be separated by single spaces. 

def WordCount(str): 
    words = str.strip().split(' ')

    # code goes here 
    return len(words)
    
# keep this function call here  
print(WordCount(raw_input()))