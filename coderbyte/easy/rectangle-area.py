# Have the function RectangleArea(strArr) take the array of strings stored in strArr, which will only contain 4 elements and be in the form (x y) where x and y are both integers, and return the area of the rectangle formed by the 4 points on a Cartesian grid. The 4 elements will be in arbitrary order. For example: if strArr is ["(0 0)", "(3 0)", "(0 2)", "(3 2)"] then your program should return 6 because the width of the rectangle is 3 and the height is 2 and the area of a rectangle is equal to the width * height.

def coords(s):
    x, y = s.replace('(','').replace(')','').split(' ')
    return int(x), int(y)

def RectangleArea(strArr):
    # Convert into coords
    points = [coords(s) for s in strArr]
    
    xs = [x[0] for x in points]
    ys = [x[1] for x in points]
    
    width = max(xs) - min(xs)
    height = max(ys) - min(ys)

    # code goes here 
    return width*height