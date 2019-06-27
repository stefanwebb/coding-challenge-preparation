# Have the function FirstReverse(str) take the str parameter being passed and return the string in reversed order. For example: if the input string is "Hello World and Coders" then your program should return the string sredoC dna dlroW olleH.

def FirstReverse(string):
    return "".join(list(reversed(string)))
    
# TODO: Version does that not make use of Python library

# keep this function call here  
print(FirstReverse(raw_input()))