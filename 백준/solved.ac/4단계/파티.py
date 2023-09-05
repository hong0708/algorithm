# https://www.acmicpc.net/problem/1238

import heapq

INF = int(1e9)

n, m, x = map(int, input().split())
arr = [[] for _ in range(n + 1)]
back = [INF for _ in range(n + 1)]
ans = 0

for _ in range(m):
    s, e, w = map(int, input().split())
    arr[s].append([e, w])

hq = []
heapq.heappush(hq, (x, 0))
back[x] = 0
while hq:
    now, road = heapq.heappop(hq)

    # 지금까지 진행한 거리가 현재 최단거리보다 크다면 진행할 필요없음
    if back[now] >= road:
        for i in arr[now]:
            # 지금까지 온 거리에 현재 경로로 해당 위치를 가는 것과
            # 기존에 해당 위치로 가는 거리를 비교
            if i[1] + road < back[i[0]]:
                back[i[0]] = i[1] + road
                heapq.heappush(hq, (i[0], i[1] + road))
for start in range(1, n + 1):
    if start == x:
        continue

    impl = [INF for _ in range(n + 1)]
    hq = []
    heapq.heappush(hq, (start, 0))
    impl[start] = 0

    while hq:
        now, road = heapq.heappop(hq)

        # 지금까지 진행한 거리가 현재 최단거리보다 크다면 진행할 필요없음
        if impl[now] >= road:
            for i in arr[now]:
                # 지금까지 온 거리에 현재 경로로 해당 위치를 가는 것과
                # 기존에 해당 위치로 가는 거리를 비교
                if i[1] + road < impl[i[0]]:
                    impl[i[0]] = i[1] + road
                    heapq.heappush(hq, (i[0], i[1] + road))
    ans = max(ans, (back[start] + impl[x]))
print(ans)
