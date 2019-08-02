# Q8.1: Triple step

# Naive solution
calls = [0]
def triple_step(n):
    # f(n) = f(n-1) + f(n-2) + f(n-3)
    calls[0] += 1

    # Base case
    if n == 0:
        return 1

    ans = 0
    if n >= 1:
        ans += triple_step(n-1)
    
    if n >= 2:
        ans += triple_step(n-2)

    if n >= 3:
        ans += triple_step(n-3)

    return ans

# Memoizing solution
memos = {0:1}
calls2 = [0]
def triple_step_memo(n):
    calls2[0] += 1

    if n in memos:
        return memos[n]

    ans = 0
    if n >= 1:
        ans += triple_step_memo(n-1)
    
    if n >= 2:
        ans += triple_step_memo(n-2)

    if n >= 3:
        ans += triple_step_memo(n-3)

    memos[n] = ans
    return ans

# Bottom-up
def triple_step_iter(n):
    ans = [1] + [0]*n

    for i in range(1,n+1):
        if i >= 1:
            ans[i] += ans[i-1]
        
        if i >= 2:
            ans[i] += ans[i-2]

        if i >= 3:
            ans[i] += ans[i-3]

    return ans[-1]


#print(triple_step(5))
#print('calls', calls[0])

print(triple_step_memo(10))
print(triple_step_iter(10))
#print('calls', calls2[0])
