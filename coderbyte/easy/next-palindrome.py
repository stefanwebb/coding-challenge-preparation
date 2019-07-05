# Have the function NextPalindrome(num) take the num parameter being passed and return the next largest palindromic number. The input can be any positive integer. For example: if num is 24, then your program should return 33 because that is the next largest number that is a palindrome. 

# TODO: Naive solution!

# Sketch of a more efficient solution
# 1. Add 1 to num
# 2. Check if current palindrome is >= num
# 3. If not, round up and return next palindrome
def makePalindrome(num):
    s = str(num)
    isodd = 1 if len(s) % 2 == 1 else 0
    right = len(s)//2
    return int(s[0:(right+isodd)] + s[0:right][::-1])

def NextPalindrome(num):
    num += 1
        
    # Round up, increasing lower bound on palindrome            
    for idx in range(0,len(str(num))):
        palindrome = makePalindrome(num)
        if palindrome >= num:
            break

        power = 10**idx
        digit = 10 - (num//power % 10)
        num += digit * power

    return palindrome

print(NextPalindrome(24))