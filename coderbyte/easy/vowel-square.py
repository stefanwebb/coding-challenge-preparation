"""
Have the function VowelSquare(strArr) take the strArr parameter being passed which will be a 2D matrix of some arbitrary size filled with letters from the alphabet, and determine if a 2x2 square composed entirely of vowels exists in the matrix. For example: strArr is ["abcd", "eikr", "oufj"] then this matrix looks like the following: 

a b c d
e i k r
o u f j 

Within this matrix there is a 2x2 square of vowels starting in the second row and first column, namely, ei, ou. If a 2x2 square of vowels is found your program should return the top-left position (row-column) of the square, so for this example your program should return 1-0. If no 2x2 square of vowels exists, then return the string not found. If there are multiple squares of vowels, return the one that is at the most top-left position in the whole matrix. The input matrix will at least be of size 2x2. 
"""

vowels = ['a', 'i', 'o', 'u', 'e']

def VowelSquare(strArr):
    rows = len(strArr)
    cols = len(strArr[0])
    
    for idx in range(rows-1):
        for jdx in range(cols-1):
            if strArr[idx][jdx] in vowels and strArr[idx+1][jdx] in vowels and strArr[idx][jdx+1] in vowels and strArr[idx+1][jdx+1] in vowels:
                return '{}-{}'.format(idx, jdx)

    # code goes here 
    return 'not found'