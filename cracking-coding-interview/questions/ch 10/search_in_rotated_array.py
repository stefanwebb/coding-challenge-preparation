# Q10.3

def search_rotated_array(arr, x):
    lower = 0
    upper = len(arr) - 1

    while lower < upper:
        median = (lower + upper) // 2

        if arr[median] < arr[lower] and (x < arr[median] or x > arr[lower]):
            upper = median - 1

        elif arr[median] > arr[upper] and (x > arr[median] or x < arr[upper]):
            lower = median + 1

        elif arr[lower] < arr[median] and arr[lower] < x  and x < arr[median]:
            upper = median - 1

        elif arr[median] < arr[upper] and arr[median] < x and x < arr[upper]:
            lower = median + 1
        
        else:
            return median, arr[median]

    return None, None

"""
Note on solution

My solution doesn't work if there are duplicate entries. (See book, pg. 399)

In general, consider the boundary cases!

"""

arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
print(search_rotated_array(arr, 5))