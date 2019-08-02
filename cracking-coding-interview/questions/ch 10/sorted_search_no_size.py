# Q10.4

def sorted_search_no_size(arr, x):
    # Calculate an upper bound on the length
    upper = 1
    while True:
        try:
            arr[upper]
            upper *= 2
        except:
            break

    # Do modified binary search
    lower = 0
    while lower < upper:
        median = (lower + upper)//2
        try:
            if x > arr[median]:
                lower = median + 1
            elif x < arr[median]:
                upper = median - 1
            else:
                return median
        except:
            upper = median-1

    return None

arr = list(sorted([1, 3, 4, 5, 7, 10, 14, 15, 16, 19, 20, 25]))

print(sorted_search_no_size(arr, 5))