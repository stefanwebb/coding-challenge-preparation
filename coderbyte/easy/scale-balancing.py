# Have the function ScaleBalancing(strArr) read strArr which will contain two elements, the first being the two positive integer weights on a balance scale (left and right sides) and the second element being a list of available weights as positive integers. Your goal is to determine if you can balance the scale by using the least amount of weights from the list, but using at most only 2 weights. For example: if strArr is ["[5, 9]", "[1, 2, 6, 7]"] then this means there is a balance scale with a weight of 5 on the left side and 9 on the right side. It is in fact possible to balance this scale by adding a 6 to the left side from the list of weights and adding a 2 to the right side. Both scales will now equal 11 and they are perfectly balanced. Your program should return a comma separated string of the weights that were used from the list in ascending order, so for this example your program should return the string 2,6 

# There will only ever be one unique solution and the list of available weights will not be empty. It is also possible to add two weights to only one side of the scale to balance it. If it is not possible to balance the scale then your program should return the string not possible. 

def strToList(s):
    return [int(i) for i in s[1:-1].split(',')]

def ScaleBalancing(strArr):
    balances = strToList(strArr[0])
    weights = strToList(strArr[1])
    
    diff = balances[0] - balances[1]
    
    # Enumerate all possible combinations of left/right weights
    for idx, w1 in enumerate(weights):
        if w1 == diff or -w1 == diff:
            return int(w1)
            
    # TODO: Can reduce n^2 loop to n by using hash table
    for idx, w1 in enumerate(weights):
        for _, w2 in enumerate(weights[idx+1:]):
            if -w1-w2 == diff or w1+w2 == diff or -w1+w2 == diff or w1-w2 == diff:
                return "{},{}".format(*list(sorted([w1,w2])))

    # code goes here 
    return 'not possible'

print(ScaleBalancing(["[3, 4]", "[1, 2, 7, 7]"]))