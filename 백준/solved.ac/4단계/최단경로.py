# https://www.acmicpc.net/problem/1753

import heapq

INF = int(1e9)

v, e = map(int, input().split())
now = int(input())
arr = [[] for _ in range(v + 1)]

ans = [INF for _ in range(v + 1)]
ans[now] = 0

for _ in range(e):
    x, y, w = map(int, input().split())
    arr[x].append([y, w])

hq = []
heapq.heappush(hq, (0, now))

while hq:
    w, loc = heapq.heappop(hq)
    # 현재까지 진행해온 w가 다른 경우로 온 w보다 크다면 볼필요없음
    if ans[loc] < w:
        continue

    for i in arr[loc]:
        if i[1] + w < ans[i[0]]:
            ans[i[0]] = i[1] + w
            heapq.heappush(hq, (i[1] + w, i[0]))

for i in range(1, v + 1):
    if ans[i] == INF:
        print('INF')
    else:
        print(ans[i])