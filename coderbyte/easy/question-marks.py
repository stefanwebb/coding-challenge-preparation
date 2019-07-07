# Have the function QuestionsMarks(str) take the str string parameter, which will contain single digit numbers, letters, and question marks, and check if there are exactly 3 question marks between every pair of two numbers that add up to 10. If so, then your program should return the string true, otherwise it should return the string false. If there aren't any two numbers that add up to 10 in the string, then your program should return false as well. 

# For example: if str is "arrb6???4xxbl5???eee5" then your program should return true because there are exactly 3 question marks between 6 and 4, and 3 question marks between 5 and 5 at the end of the string. 

def countMarks(s):
    count = 0
    for c in s:
        if c == '?':
            count += 1
    return count

def QuestionsMarks(s):
    idx = 0
    
    # Extract all the digit locations
    locs = []
    for idx in range(len(s)):
        # Found the start of a pair
        if s[idx].isdigit():
            locs.append(idx)
            
    # Check consecutive pairs
    returnTrue = False
    for idx in range(len(locs)-1):
        if int(s[locs[idx]]) + int(s[locs[idx+1]]) == 10:
            returnTrue = True
            if not countMarks(s[(locs[idx]+1):locs[idx+1]]) == 3:
                return 'false'

    # code goes here 
    if returnTrue:
        return 'true'
    else:
        return 'false'

print(QuestionsMarks("acc?7??sss?3rr1??????5"))