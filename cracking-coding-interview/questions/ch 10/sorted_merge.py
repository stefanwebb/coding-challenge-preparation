# Q10.1: Sorted merge

def sorted_merge(A, B):
    ans = []

    i = j = 0
    while i < len(A) or j < len(B):
        if i >= len(A):
            ans.append(B[j])
            j += 1
        elif j >= len(B):
            ans.append(A[i])
            i += 1
        elif A[i] <= B[j]:
            ans.append(A[i])
            i += 1
        else:
            ans.append(B[j])
            j += 1

    return ans

A = list(sorted([3, 6, 9, 6, 2, 4]))
B = list(sorted([7, 8, 1]))

print(A, B)
print(sorted_merge(A, B))