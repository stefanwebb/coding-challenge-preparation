# Q1.7

import copy

# Version that makes a copy
def rotate_matrix(M):
    ans = copy.deepcopy(M)
    N = len(M)
    for jdx in range(N):
        for idx in range(N):
            ans[jdx][idx] = M[N-idx-1][jdx]
            
    return ans

M1 = [[0,1], [2, 3]]
M2 = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

# Version that operates in-place

def rotate_matrix2(M):
    N = len(M)
    
    # Take transpose
    for jdx in range(0,N):
        for idx in range(jdx+1, N):
            M[jdx][idx], M[idx][jdx] = M[idx][jdx], M[jdx][idx]
    
    # flip columns
    for jdx in range(0, N):
        for idx in range(0, N//2):
            M[jdx][idx], M[jdx][N-idx-1] = M[jdx][N-idx-1], M[jdx][idx]
    
    return M

"""
Notes on solutions

There is an alternative version that swaps four points at a time! Redo with this solution.

"""

print(rotate_matrix(M1))
print(rotate_matrix2(M1))