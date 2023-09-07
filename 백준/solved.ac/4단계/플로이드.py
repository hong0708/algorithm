# https://www.acmicpc.net/problem/11404

import heapq

INF = int(1e9)

n = int(input())
m = int(input())

arr = [[] for _ in range(n + 1)]
ans = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])

for i in range(1, n + 1):
    ans[i][i] = 0
    hq = []
    heapq.heappush(hq, (i, 0))
    while hq:
        now, w = heapq.heappop(hq)

        if ans[i][now] >= w:
            for j in arr[now]:
                if ans[i][j[0]] >= w + j[1]:
                    ans[i][j[0]] = w + j[1]
                    heapq.heappush(hq, (j[0], ans[i][j[0]]))

for i in range(n+1):
    for j in range(n+1):
        if ans[i][j] == INF:
            ans[i][j] = 0

for q in range(1, n + 1):
    print(*ans[q][1:])
