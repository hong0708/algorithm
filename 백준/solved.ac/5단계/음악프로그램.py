# https://www.acmicpc.net/problem/2623

import sys
from collections import deque

n, m = map(int, input().split())
arr = [0 for _ in range(n + 1)]
r = [[] for _ in range(n + 1)]
ans = []

for _ in range(m):
    impl = list(map(int, sys.stdin.readline().split()))
    dg = 1
    for i in range(2, len(impl)):
        arr[impl[i]] += 1
        dg += 1
        r[impl[i - 1]].append(impl[i])

dq = deque()
for i in range(1, n + 1):
    if arr[i] == 0:
        dq.append(i)

while dq:
    now = dq.popleft()
    ans.append(now)
    for i in r[now]:
        arr[i] -= 1
        if arr[i] == 0:
            dq.append(i)
if len(ans) == n:
    for i in ans:
        print(i)
else:
    print(0)
