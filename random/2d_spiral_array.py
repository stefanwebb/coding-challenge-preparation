# This question is taken from the Facebook interview examples
import numpy as np

def spiral(n):
    ans = np.zeros((n, n))

    # Number of spirals
    first_elem = 1
    for idx_spiral in range((n-1)//2+1):
        for jdx_column in range(idx_spiral, n-idx_spiral-1):
            spiral_width = n-2*idx_spiral-1

            ans[idx_spiral, jdx_column] = first_elem + jdx_column - idx_spiral
            ans[jdx_column, n-idx_spiral-1] = first_elem + jdx_column - idx_spiral + spiral_width
            ans[n-idx_spiral-1, n-jdx_column-1] = first_elem + jdx_column - idx_spiral + 2*spiral_width
            ans[n-jdx_column-1, idx_spiral] = first_elem + jdx_column - idx_spiral + 3*spiral_width

        first_elem += 4*(n - 1 - 2*idx_spiral)
        
    return ans

print(spiral(8))