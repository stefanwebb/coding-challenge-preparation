# Have the function VowelCount(str) take the str string parameter being passed and return the number of vowels the string contains (ie. "All cows eat grass and moo" would return 8). Do not count y as a vowel for this challenge. 

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

def VowelCount(str): 
    countVowels = 0
    
    for c in str:
        if c in vowels:
            countVowels += 1

    # code goes here 
    return countVowels
    
# keep this function call here  
print(VowelCount(raw_input()))