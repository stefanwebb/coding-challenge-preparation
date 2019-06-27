# Have the function SimpleSymbols(str) take the str parameter being passed and determine if it is an acceptable sequence by either returning the string true or false. The str parameter will be composed of + and = symbols with several letters between them (ie. ++d+===+c++==a) and for the string to be true each letter must be surrounded by a + symbol. So the string to the left would be false. The string will not be empty and will have at least one letter.

def SimpleSymbols(str):
    for i in range(len(str)):
        char = str[i]

        if char.isalpha():
            # First and last characters can't be letters
            if (i == 0 or i == len(str)-1):
                return 'false'
            
            # Other letters must be enclosed in '+'
            elif not (str[i-1] == '+' and str[i+1] == '+'):
                return 'false'
        

    # code goes here 
    return 'true'
    
# keep this function call here  
print(SimpleSymbols(raw_input()))