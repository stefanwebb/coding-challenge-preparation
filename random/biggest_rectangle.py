# Find the rectangle at the origin with the biggest sum
import numpy as np

arr = np.array([[6, 5, -9, 2], [-2, -5, -2, 7], [3, -2, 10, 13], [-8, -3, 1, -2]])

def biggest_rectangle(arr):
    ans = np.zeros_like(arr)
    max_ans = arr[0, 0]
    
    for idx in range(0, arr.shape[0]):
        for jdx in range(0, arr.shape[1]):
            ans[idx, jdx] = arr[idx, jdx]

            if idx > 0:
                ans[idx, jdx] += ans[idx-1, jdx]

            if jdx > 0:
                ans[idx, jdx] += ans[idx, jdx-1]

            if jdx > 0 and idx > 0:
                ans[idx, jdx] -= ans[idx-1,jdx-1]

            if ans[idx, jdx] > max_ans:
                max_ans = ans[idx, jdx]

    print(ans)

    # TODO: Return max
    return max_ans

print(biggest_rectangle(arr))