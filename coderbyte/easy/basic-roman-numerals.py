# Have the function BasicRomanNumerals(str) read str which will be a string of Roman numerals. The numerals being used are: I for 1, V for 5, X for 10, L for 50, C for 100, D for 500 and M for 1000. In Roman numerals, to create a number like 11 you simply add a 1 after the 10, so you get XI. But to create a number like 19, you use the subtraction notation which is to add an I before an X or V (or add an X before an L or C). So 19 in Roman numerals is XIX. 

# The goal of your program is to return the decimal equivalent of the Roman numeral given. For example: if str is "XXIV" your program should return 24 

specialCases = { 'CM':900, 'XC':90, 'IX': 9, 'XL':40, 'CD':400, 'IV':4 }
regularCases = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

def BasicRomanNumerals(s):
    num = 0
    
    # Thousands
    idx = 0
    while idx < len(s):
        # Check special cases
        if idx < len(s)-1:
            substr = s[idx:(idx+2)]
            if substr in specialCases:
                num += specialCases[substr]
                idx += 2
                continue
        
        # Regular cases
        num += regularCases[s[idx]]
        idx += 1

    # code goes here 
    return num