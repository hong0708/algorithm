# https://www.acmicpc.net/problem/2467

import sys

n = int(input())
w = list(map(int, sys.stdin.readline().split()))
s = 0
e = n - 1
ans = 1000000000
result = [0, n - 1]

while s < e:
    res = w[e] + w[s]
    if ans > abs(res):
        ans = abs(res)
        result[0], result[1] = w[s], w[e]

    if res > 0:
        e -= 1
    elif res < 0:
        s += 1
    else:
        break
print(*result)
