# Have the function OtherProducts(arr) take the array of numbers stored in arr and return a new list of the products of all the other numbers in the array for each element. For example: if arr is [1, 2, 3, 4, 5] then the new array, where each location in the new array is the product of all other elements, is [120, 60, 40, 30, 24]. The following calculations were performed to get this answer: [(2*3*4*5), (1*3*4*5), (1*2*4*5), (1*2*3*5), (1*2*3*4)]. You should generate this new array and then return the numbers as a string joined by a hyphen: 120-60-40-30-24. The array will contain at most 10 elements and at least 1 element of only positive integers. 

# TODO: Better than n^2 version?
# Look for duplicate calculations!
def OtherProducts(arr):
    products = [1]*len(arr)
    for idx in range(len(arr)):
        for jdx in range(len(arr)):
            if idx == jdx:
                continue
            products[jdx] *= arr[idx]
    
    ans = '-'.join([str(p) for p in products])

    # code goes here 
    return ans