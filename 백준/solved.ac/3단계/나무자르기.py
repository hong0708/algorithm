# https://www.acmicpc.net/problem/2805

import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()
ans = 0


def c(x):
    res = 0
    for i in arr:
        if i > x:
            res += (i - x)
        if res >= m:
            return True
    return False


start = 0
end = arr[-1]

while start <= end:
    a = (start + end) // 2

    if c(a):
        ans = max(ans, a)
        start = a + 1
    else:
        end = a - 1
print(ans)