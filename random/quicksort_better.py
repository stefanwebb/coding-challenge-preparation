def quicksort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot = arr[high]
        jdx = low
        for idx in range(low, high):
            if arr[idx] < pivot:
                arr[idx], arr[jdx] = arr[jdx], arr[idx]
                jdx += 1
        arr[jdx], arr[high] = arr[high], arr[jdx]

        # Recurse
        quicksort(arr, low, jdx-1)
        quicksort(arr, jdx+1, high)

def find_k(arr, k, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot = arr[high]
        jdx = low
        for idx in range(low, high):
            if arr[idx] < pivot:
                arr[idx], arr[jdx] = arr[jdx], arr[idx]
                jdx += 1
        arr[jdx], arr[high] = arr[high], arr[jdx]

        # Recurse
        if jdx == k:
            return arr[jdx]
        elif jdx > k:
            find_k(arr, k, low, jdx-1)
        else:
            find_k(arr, k, jdx+1, high)

arr = [0, 5, 8, 3, 2, 3, 5, 8, 6]
quicksort(arr)
print(arr)