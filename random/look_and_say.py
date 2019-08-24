def look_and_say(s):
    ans = []

    idx = 0
    while idx < len(s):
        count = 1
        char = s[idx]
        idx += 1

        while idx < len(s) and s[idx] == char:
            count += 1
            idx += 1

        ans.extend([str(count),char])

    return ''.join(ans)

init = '1'

for _ in range(10):
    init = look_and_say(init)
    print(init)