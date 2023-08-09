# https://www.acmicpc.net/problem/17298

from collections import deque

n = int(input())
arr = list(map(int, input().split()))
ans = [-1 for _ in range(n)]

d = deque()
for i in range(n):
    while d and d[-1][1] < arr[i]:
        c = d.pop()
        ans[c[0]] = arr[i]
    d.append([i, arr[i]])
print(*ans)
