# Top-down merge sort
def merge(arr1, arr2):
    ans = []
    i = j = 0
    while i < len(arr1) or j < len(arr2):
        if i == len(arr1):
            ans.append(arr2[j])
            j += 1
        elif j == len(arr2):
            ans.append(arr1[i])
            i += 1
        else:
            if arr1[i] < arr2[j]:
                ans.append(arr1[i])
                i += 1
            else:
                ans.append(arr2[j])
                j += 1

    return ans

def merge_sort(arr):
    # Base case
    if len(arr) == 1:
        return arr

    halfway = len(arr)//2
    left = merge_sort(arr[:halfway])
    right = merge_sort(arr[halfway:])

    return merge(left, right)

# TODO: Bottom-up version

# Trying it out
x = [7, 3, 8, 7, 2, 9, 8, 1, 0]
print(merge_sort(x))