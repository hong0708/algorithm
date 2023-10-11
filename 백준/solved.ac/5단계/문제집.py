# https://www.acmicpc.net/problem/1766

import heapq

n, m = map(int, input().split())
arr = [[] for _ in range(n + 1)]
dg = [0 for _ in range(n + 1)]
res = []

for _ in range(m):
    s, e = map(int, input().split())
    dg[e] += 1
    arr[s].append(e)

dq = []
for i in range(n, 0, -1):
    if dg[i] == 0:
        heapq.heappush(dq, i)

while dq:
    now = heapq.heappop(dq)
    if dg[now] == 0:
        res.append(now)
    for i in arr[now]:
        dg[i] -= 1
        if dg[i] == 0:
            heapq.heappush(dq,i)
print(*res)
