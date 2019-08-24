arr = [0, 5, 8, 3, 2, 3, 5, 8, 6]

# O(n*lg(n)) solution
def naive_k(arr, k):
    assert k >= 0 and k < len(arr)

    # Create copy rather than doing in place
    arr = sorted(arr)

    return arr[k]

# Average runtime O(lg(n)) solution that uses modification of quicksort
def quick_k(arr, k, start=0, end=None):
    assert k >= 0 and k < len(arr)

    if end is None:
        end = len(arr)

    #if end >= k:
    #    return arr[k]

    # TODO: Choose pivot 
    pivot = end - 1
    jdx = start

    for idx in range(start, end):
        if arr[idx] < arr[pivot]:
            if k != idx:
                arr[idx], arr[jdx] = arr[jdx], arr[idx]
            jdx += 1
    arr[pivot], arr[jdx] = arr[jdx], arr[pivot]

    # Here's the crucial difference between quicksort and "quick kth"
    # Only recurse on side which k is in
    #if jdx == k:
    #    return arr[jdx]
    if jdx < k:
        return quick_k(arr, k, jdx+1, end)
    else:
        return quick_k(arr, k, start, jdx)

#print(naive_k(arr, 8))

for k in range(len(arr)):
    arr = [0, 5, 8, 3, 2, 3, 5, 8, 6]
    print(quick_k(arr, k))