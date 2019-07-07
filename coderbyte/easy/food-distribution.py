# Have the function FoodDistribution(arr) read the array of numbers stored in arr which will represent the hunger level of different people ranging from 0 to 5 (0 meaning not hungry at all, 5 meaning very hungry). You will also have N sandwiches to give out which will range from 1 to 20. The format of the array will be [N, h1, h2, h3, ...] where N represents the number of sandwiches you have and the rest of the array will represent the hunger levels of different people. Your goal is to minimize the hunger difference between each pair of people in the array using the sandwiches you have available. 

# For example: if arr is [5, 3, 1, 2, 1], this means you have 5 sandwiches to give out. You can distribute them in the following order to the people: 2, 0, 1, 0. Giving these sandwiches to the people their hunger levels now become: [1, 1, 1, 1]. The difference between each pair of people is now 0, the total is also 0, so your program should return 0. Note: You may not have to give out all, or even any, of your sandwiches to produce a minimized difference. 

# Another example: if arr is [4, 5, 2, 3, 1, 0] then you can distribute the sandwiches in the following order: [3, 0, 1, 0, 0] which makes all the hunger levels the following: [2, 2, 2, 1, 0]. The differences between each pair of people is now: 0, 0, 1, 1 and so your program should return the final minimized difference of 2. 

# This greedy solution doesn't quite seem to work...
def FoodDistribution(arr):
    sandwiches = arr[0]
    hungers = arr[1:]
    countPeople = len(hungers)
    
    for jdx in range(sandwiches):
        maxDiff = -2
        maxIdx = -1

        for idx in range(countPeople):
            # Work out the change of giving a sandwich to each person
            diff = 0
            if idx < countPeople-1:
                diff += 1 if hungers[idx] > hungers[idx+1] else -1
            if idx > 0:
                diff += 1 if hungers[idx] > hungers[idx-1] else -1
            if diff > maxDiff:
                maxDiff = diff
                maxIdx = idx
            
        if maxDiff >= 0:
            hungers[maxIdx] -= 1
        else:
            break
            
    # Calculate result
    diffs = []
    for jdx in range(len(hungers)-1):
        diffs.append(abs(hungers[jdx] - hungers[jdx+1]))

    # code goes here 
    return sum(diffs)

# This is another user's solution
# TODO: Understand it!
def FoodDistribution2(arr): 
    sandwiches = arr[0]
    scanning = True
    
    while scanning:
        scanning = False
        for n in range(2, len(arr)-1):
            if arr[n] > arr[n+1] and arr[n] > arr[n-1] and sandwiches > 0:
                scanning = True
                arr[n] -= 1
                sandwiches -= 1
    
    scanning = True
    
    while sandwiches > 0 and  arr[1] > arr[2]:
            arr[1] -= 1
            sandwiches -= 1
    
    while sandwiches > 0 and arr[-1] > arr[-2]:
            arr[-1] -= 1
            sandwiches -= 1
    
    while scanning:
        scanning = False
        for n in range(1, len(arr)):
            if n == 1:
                if arr[n] > arr[n+1] and sandwiches > 0:
                    scanning = True
                    arr[n] -= 1
                    sandwiches -= 1
            if n == len(arr) - 1:
                if arr[n] > arr[n-1] and sandwiches >0:
                    scanning = True
                    arr[n] -= 1
                    sandwiches -= 1
            elif arr[n] > arr[n-1] or arr[n] > arr[n+1]:
                if sandwiches > 0:
                    scanning = True
                    arr[n] -= 1
                    sandwiches -= 1
    
    diff = 0
    
    for n in range(1, len(arr)-1):
        diff += abs(arr[n]-arr[n+1])
        
    return diff
    
print(FoodDistribution([7, 5, 4, 3, 4, 5, 2, 3, 1, 4, 5]))