def NumberAddition(s):
    # Extract numbers
    numbers = []
    i = 0
    while True:
        # Skip nonwords
        while i < len(s) and not s[i].isdigit():
            i += 1

        numString = []            
        # Extract number
        while i < len(s) and s[i].isdigit():
            numString.append(s[i])
            i += 1
            
        if len(numString):
            numbers.append(int(''.join(numString)))
        
        if i >= len(s):
            break

    # Add them together
    return sum(numbers)

print(NumberAddition("10 2One Number*1*"))