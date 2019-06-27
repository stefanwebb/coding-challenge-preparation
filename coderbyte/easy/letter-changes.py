# Have the function LetterChanges(str) take the str parameter being passed and modify it using the following algorithm. Replace every letter in the string with the letter following it in the alphabet (ie. c becomes d, z becomes a). Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string.

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

def LetterChanges(str):
    newString = []
    
    for c in str:
        if not c.isalpha():
            newString.append(c)
        else:
            if c == 'z':
                c = 'a'
            else:
                c = chr(ord(c)+1)
                if c in vowels:
                    c = c.upper()
            newString.append(c)

    # code goes here 
    return "".join(newString)
    
# keep this function call here  
print(LetterChanges(raw_input()))