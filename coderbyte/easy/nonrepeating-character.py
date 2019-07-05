# Have the function NonrepeatingCharacter(str) take the str parameter being passed, which will contain only alphabetic characters and spaces, and return the first non-repeating character. For example: if str is "agettkgaeee" then your program should return k. The string will always contain at least one character and there will always be at least one non-repeating character. 

def NonrepeatingCharacter(str):
    # Count characters
    charCounts = {}
    charIdx = {}
    for idx, char in enumerate(str):
        charCounts.setdefault(char, 0)
        charIdx.setdefault(char, idx)
        charCounts[char] = charCounts[char] + 1
    
    # Filter nonrepeating characters
    chars = [c for c,v in charCounts.items() if v == 1]
    minChar = None
    minIdx = len(str)+1
    for char, idx in charIdx.items():
        if char in chars and idx < minIdx:
            minIdx = idx
            minChar = char

    # code goes here
    return minChar