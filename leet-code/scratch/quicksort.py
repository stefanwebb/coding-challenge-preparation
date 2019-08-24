# Implementation of simple quicksort

def quicksort(arr, start=0, end=None):
    if end is None:
        end = len(arr)

    # Pivot on last element
    # TODO: Choose element at random
    k = end - 1

    jdx = start
    for idx in range(start, end):
        if arr[idx] < arr[k]:
            # Swap this element with the head of the right side of the pivot
            if k != idx:
                arr[jdx], arr[idx] = arr[idx], arr[jdx]
            jdx += 1

    # Place pivot
    arr[jdx], arr[k] = arr[k], arr[jdx]

    # Pivot on two halves
    if jdx > 1: 
        quicksort(arr, start, jdx)

    if k-jdx > 2:
        quicksort(arr, jdx+1, end)

arr = [0, 5, 8, 3, 2, 3, 5, 8, 6]
quicksort(arr)

print(arr)


"""

Notes on solution: Slicing an array seems to create a new array!

"""