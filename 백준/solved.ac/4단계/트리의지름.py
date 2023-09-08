# https://www.acmicpc.net/problem/1967

import heapq

INF = 1e9

n = int(input())
arr = [[] for _ in range(n + 1)]
level = [[] for _ in range(n + 1)]
ans = 0

for i in range(n - 1):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])
    arr[b].append([a, c])

impl = [INF for _ in range(n + 1)]
impl[1] = 0
hq = []
heapq.heappush(hq, (1, 0))
while hq:
    now, w = heapq.heappop(hq)
    if w <= impl[now]:
        for x in arr[now]:
            if impl[x[0]] >= w + x[1]:
                impl[x[0]] = w + x[1]
                heapq.heappush(hq, (x[0], impl[x[0]]))

where = impl.index(max(impl[1:]))

impl = [INF for _ in range(n + 1)]
impl[where] = 0
hq = []
heapq.heappush(hq, (where, 0))
while hq:
    now, w = heapq.heappop(hq)
    if w <= impl[now]:
        for x in arr[now]:
            if impl[x[0]] >= w + x[1]:
                impl[x[0]] = w + x[1]
                heapq.heappush(hq, (x[0], impl[x[0]]))

print(max(impl[1:]))
