# Have the function EvenPairs(str) take the str parameter being passed and determine if a pair of adjacent even numbers exists anywhere in the string. If a pair exists, return the string true, otherwise return false. For example: if str is "f178svg3k19k46" then there are two even numbers at the end of the string, "46" so your program should return the string true. Another example: if str is "7r5gg812" then the pair is "812" (8 and 12) so your program should return the string true.

def EvenPairs(str):
    starts = set()
    ends = set()
    
    # Search for all even numbers in string
    for i in range(len(str)):
        for j in range(i,len(str)):
            if not str[j].isdigit():
                break
            if int(str[i:(j+1)]) % 2 == 0:
                starts.add(i)
                ends.add(j+1)
            
    # Check whether adjacent
    for i in starts:
        if i in ends:
            return 'true'

    # code goes here 
    return 'false'