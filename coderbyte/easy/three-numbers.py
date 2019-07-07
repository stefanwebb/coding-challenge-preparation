# Have the function ThreeNumbers(str) take the str parameter being passed and determine if exactly three unique, single-digit integers occur within each word in the string. The integers can appear anywhere in the word, but they cannot be all adjacent to each other. If every word contains exactly 3 unique integers somewhere within it, then return the string true, otherwise return the string false. For example: if str is "2hell6o3 wor6l7d2" then your program should return "true" but if the string is "hell268o w6or2l4d" then your program should return "false" because all the integers are adjacent to each other in the first word. Use the Parameter Testing feature in the box below to test your code with different arguments.

def ThreeNumbers(str):
    words = str.split(' ')
    
    for word in words:
        locs = []
        nums = set()
        
        for idx, char in enumerate(word):
            if char.isdigit():
                locs.append(idx)
                nums.insert(int(char))
        
        if len(nums) != 3:
            return 'false'
        
        if locs[1] - locs[0] == 1 and locs[2] - locs[1] == 1:
            return 'false'

    # code goes here 
    return 'true'

print(ThreeNumbers("2a3b5 w1o2rl3d g1gg92"))