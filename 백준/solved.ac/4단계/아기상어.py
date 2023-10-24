# https://www.acmicpc.net/problem/16236

import sys
from collections import deque

# 가장 위, 가장 왼쪽
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n = int(sys.stdin.readline().rstrip())
arr = []

for i in range(n):
    impl = list(map(int, sys.stdin.readline().split()))
    if 9 in impl:
        a, b = i, impl.index(9)
        impl[b] = 0
    arr.append(impl)

eat = 0
baby = 2
time = 0
end = True
while end:
    call = True
    loc = deque()
    loc.append([a, b, baby, eat, time])

    # 현재 위치
    while loc:
        now_loc = loc.popleft()
        # 현재 위치 기준으로 다음 갈 장소 탐색
        dq = deque()
        dq.append([now_loc[0], now_loc[1], now_loc[2], now_loc[3], now_loc[4]])

        visited = [[False for _ in range(n)] for _ in range(n)]
        call = True
        while call and dq:
            now = dq.popleft()
            x, y, bs, e, t = now[0], now[1], now[2], now[3], now[4]
            call = True
            # 먼저 최대한 위 그리고 왼쪽을 본다 먹이 우선 순위 때문에
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 길을 갈 수 있으면 간다
                if -1 < nx < n and -1 < ny < n and not visited[nx][ny] and arr[nx][ny] <= bs:
                    # 먹을 수 있는 물고기 있는 곳이라면
                    if 0 < arr[nx][ny] < bs:
                        if e + 1 == bs:
                            loc.append([nx, ny, bs + 1, 0, t + 1])
                        else:
                            loc.append([nx, ny, bs, e + 1, t + 1])
                        arr[nx][ny] = 0
                        call = False
                        break
                    # 먹을 수 없거나 그냥 길이라면 그냥 간다.
                    else:
                        dq.append([nx, ny, bs, e, t + 1])
                        visited[nx][ny] = True

        # 다음 길들을 확인했는데 더이상 먹을 수 있는 케이스가 없음
        if call:
            print(now_loc[4])
            end = False
