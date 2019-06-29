# Have the function SwapCase(str) take the str parameter and swap the case of each character. For example: if str is "Hello World" the output should be hELLO wORLD. Let numbers and symbols stay the way they are. 

def flipCase(x):
    if x.isupper():
        return x.lower()
    else:
        return x.upper()

def SwapCase(s):
    letters = [ x if not x.isalpha() else flipCase(x) for x in s ]
    return ''.join(letters)