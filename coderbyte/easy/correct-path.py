# Have the function CorrectPath(str) read the str parameter being passed, which will represent the movements made in a 5x5 grid of cells starting from the top left position. The characters in the input string will be entirely composed of: r, l, u, d, ?. Each of the characters stand for the direction to take within the grid, for example: r = right, l = left, u = up, d = down. Your goal is to determine what characters the question marks should be in order for a path to be created to go from the top left of the grid all the way to the bottom right without touching previously travelled on cells in the grid. 

# For example: if str is "r?d?drdd" then your program should output the final correct string that will allow a path to be formed from the top left of a 5x5 grid to the bottom right. For this input, your program should therefore return the string rrdrdrdd. There will only ever be one correct path and there will always be at least one question mark within the input string. 

# NOTE: I found this question took a long time to answer!
# One thing that caught me out was that you need to make copies of mutable structures when passing as arguments to recursion...

def validMove(move, touched, location):
    if move == 'l':
        return location[0] > 0 and not touched[location[0]-1 + 5*location[1]]
    elif move == 'r':
        return location[0] < 4 and not touched[location[0]+1 + 5*location[1]]
    elif move == 'u':
        return location[1] > 0 and not touched[location[0] + 5*(location[1]-1)]
    elif move == 'd':
        return location[1] < 4 and not touched[location[0] + 5*(location[1]+1)]
    
def possibleMoves(touched, location):
    moves = []
    for m in ['u', 'r', 'd', 'l']:
        if validMove(m, touched, location):
            moves.append(m)
    return moves

def unmakeMove(move, touched, location):
    if move == 'l':
        touched[location[0] + 5*location[1]] = False
        return (location[0]+1, location[1])
    elif move == 'r':
        touched[location[0] + 5*location[1]] = False
        return (location[0]-1, location[1])
    elif move == 'u':
        touched[location[0] + 5*location[1]] = False
        return (location[0], location[1]+1)
    elif move == 'd':
        touched[location[0] + 5*location[1]] = False
        return (location[0], location[1]-1)
    
def makeMove(move, touched, location):
    if move == 'l':
        touched[location[0]-1 + 5*location[1]] = True
        return (location[0]-1, location[1])
    elif move == 'r':
        touched[location[0]+1 + 5*location[1]] = True
        return (location[0]+1, location[1])
    elif move == 'u':
        touched[location[0] + 5*(location[1]-1)] = True
        return (location[0], location[1]-1)
    elif move == 'd':
        touched[location[0] + 5*(location[1]+1)] = True
        return (location[0], location[1]+1)
        
def CorrectPath(s):
    touched = [True] + [False]*24
    
    def helper(traversed, remainder, touched, location):
        # Check if successfully reached end
        if remainder == '':
            if location == (4,4):
                return traversed
            else:
                return None
                
        move = remainder[0]
        if move != '?' and validMove(move, touched, location):
            newTouched = touched[:]
            location = makeMove(move, newTouched, location)
            return helper(traversed+move,  remainder[1:], newTouched, location)
        elif move == '?':
            moves = possibleMoves(touched, location)
            ans = None
            for m in moves:
                newTouched = touched[:]
                newLocation = makeMove(m, newTouched, location)
                h = helper(traversed+m, remainder[1:], newTouched, newLocation)
                if h != None:
                    return h
                touched[newLocation[0] + 5*newLocation[1]] = False
            return ans
        else:
            touched[location[0] + 5*location[1]] = False
            return None

    # code goes here 
    return helper('', s, touched, (0,0))

print(CorrectPath("???rrurdr?"))