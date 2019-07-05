# Have the function PalindromeCreator(str) take the str parameter being passed and determine if it is possible to create a palindromic string of minimum length 3 characters by removing 1 or 2 characters. For example: if str is "abjchba" then you can remove the characters jc to produce "abhba" which is a palindrome. For this example your program should return the two characters that were removed with no delimiter and in the order they appear in the string, so jc. If 1 or 2 characters cannot be removed to produce a palindrome, then return the string not possible. If the input string is already a palindrome, your program should return the string palindrome. 

# The input will only contain lowercase alphabetic characters. Your program should always attempt to create the longest palindromic substring by removing 1 or 2 characters (see second sample test case as an example). The 2 characters you remove do not have to be adjacent in the string. 

def isPalindrome(s):
    left = (len(s)+1)//2
    right = len(s)//2
    return s[0:left] == s[right:][::-1]

def PalindromeCreator(s):
    if len(s) >= 3 and isPalindrome(s):
        return 'palindrome'
        
    if len(s) < 3:
        return 'not possible'
        
    # Remove 1 character
    for idx in range(len(s)):
        removed = s[idx]
        substring = s[0:idx] + s[(idx+1):]
        if isPalindrome(substring):
            return removed
            
    # Remove 2 characters
    for idx in range(len(s)-1):
        for jdx in range(idx+1, len(s)):
            r1, r2 = s[idx], s[jdx]
            substring = s[0:idx] + s[(idx+1):jdx] + s[(jdx+1):]
            if isPalindrome(substring):
                return r1+r2

    # code goes here 
    return 'not possible'

print(PalindromeCreator('abjchba'))