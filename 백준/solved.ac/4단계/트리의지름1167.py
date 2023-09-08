# https://www.acmicpc.net/problem/1167

import heapq

INF = 1e9
n = int(input())
arr = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    impl = list(map(int, input().split()))
    for j in range(1, len(impl), 2):
        if impl[j] == -1:
            break
        arr[impl[0]].append([impl[j], impl[j + 1]])

impl = [INF for _ in range(n + 1)]
impl[1] = 0
hq = []
heapq.heappush(hq, (1, 0))
while hq:
    now, w = heapq.heappop(hq)
    if impl[now] >= w:
        for i in arr[now]:
            if impl[i[0]] >= w + i[1]:
                impl[i[0]] = w + i[1]
                heapq.heappush(hq, (i[0], impl[i[0]]))
where = impl.index(max(impl[1:]))

impl = [INF for _ in range(n + 1)]
impl[where] = 0
hq = []
heapq.heappush(hq, (where, 0))
while hq:
    now, w = heapq.heappop(hq)
    if impl[now] >= w:
        for i in arr[now]:
            if impl[i[0]] >= w + i[1]:
                impl[i[0]] = w + i[1]
                heapq.heappush(hq, (i[0], impl[i[0]]))

print(max(impl[1:]))
