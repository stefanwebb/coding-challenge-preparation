# Q1.8

import copy

def zero_matrix(M):
    ans = copy.deepcopy(M)
    idx = 0
    jdx = 0
    for jdx in range(len(M)):
        for idx in range(len(M[0])):
            if M[jdx][idx] == 0:
                # Kill row and column
                for kdx in range(0, len(M[0])):
                    ans[jdx][kdx] = 0
                for kdx in range(0, len(M)):
                    ans[kdx][idx] = 0
                    
    return ans

# In-place version
def zero_matrix2(X):
    M = len(X)
    N = len(X[0])
    
    rowZeros = [False]*M
    columnZeros = [False]*N
    
    for jdx in range(M):
        for idx in range(N):
            if X[jdx][idx] == 0:
                rowZeros[jdx] = True
                columnZeros[idx] = True
    
    for jdx in range(M):
        for idx in range(N):
            if rowZeros[jdx] or columnZeros[idx]:
                X[jdx][idx] = 0
    
    return X

X = [[1, 2, 3], [4, 0, 0]]
print(zero_matrix(X), zero_matrix2(X))