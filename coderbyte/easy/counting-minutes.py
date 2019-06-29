# Have the function CountingMinutesI(str) take the str parameter being passed which will be two times (each properly formatted with a colon and am or pm) separated by a hyphen and return the total number of minutes between the two times. The time will be in a 12 hour clock format. For example: if str is 9:00am-10:00am then the output should be 60. If str is 1:00pm-11:00am the output should be 1320.

def convert24h(str):
    am_pm = str[-2:]
    hours, mins = str[:-2].split(':')
    hours = int(hours)
    mins = int(mins)
    
    if str[-2:] == 'am':
        if hours == 12:
            return 0, mins
        else:
            return hours, mins
    else:
        if hours == 12:
            return 12, mins
        else:
            return hours+12, mins

def CountingMinutesI(str):
    time1, time2 = str.split('-')
    
    h1, m1 = convert24h(time1)
    h2, m2 = convert24h(time2)
    
    mins1 = h1*60 + m1
    mins2 = h2*60 + m2
    
    if mins2 - mins1 >= 0:
        return mins2 - mins1
    else:
        return 24*60 - mins1 + mins2