# Q10.5 Sparse search

def sparse_search(arr, x):
    lower = 0
    upper = len(arr) - 1

    while lower < upper:
        # Skip empty strings
        while arr[lower] == '' and lower < upper:
            lower += 1

        while arr[upper] == '' and lower < upper:
            upper -= 1
            
        median = (lower + upper)//2
        while arr[median] == '' and lower <= median:
            median -= 1

        if arr[median] < x:
            lower = median + 1
        elif arr[median] > x:
            upper = median - 1
        else:
            return median

    return None

arr = ['at', '', '', '', 'ball', '', '', 'car', '', '', 'dad', '', '']
print(sparse_search(arr, 'ball'))