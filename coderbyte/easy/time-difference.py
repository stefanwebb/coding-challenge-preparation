# Have the function TimeDifference(strArr) read the array of strings stored in strArr which will be an unsorted list of times in a twelve-hour format like so: HH:MM(am/pm). Your goal is to determine the smallest difference in minutes between two of the times in the list. For example: if strArr is ["2:10pm", "1:30pm", "10:30am", "4:42pm"] then your program should return 40 because the smallest difference is between 1:30pm and 2:10pm with a difference of 40 minutes. The input array will always contain at least two elements and all of the elements will be in the correct format and unique. 

def toMins(s):
    pm = True if s[-2:] == 'pm' else False
    s = s[:-2]
    
    hours, mins = [int(i) for i in s.split(':')]
    
    if pm and hours != 12:
        hours += 12
    elif (not pm) and hours == 12:
        hours = 0
        
    return hours*60 + mins
        
def TimeDifference(strArr):
    mins = [toMins(s) for s in strArr]
    
    minDiff = 10000
    
    for idx, t1 in enumerate(mins):
        # TODO: Can I reduce this from O(n^2) to O(nlog(n))?
        for _, t2 in enumerate(mins[(idx+1):]):
            t = abs(t1 - t2)
            t = min(1440 - t, t)
            if t < minDiff:
                minDiff = t

    # code goes here 
    return minDiff