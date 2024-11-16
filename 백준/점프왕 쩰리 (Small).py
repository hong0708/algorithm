from collections import deque

dx = [1, 0]
dy = [0, 1]

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

d = deque()
d.append([0, 0])
ans = False
while d:
    x, y = d.popleft()
    s = arr[x][y]
    if s == -1:
        print("HaruHaru")
        ans = True
        break
    elif s == 0:
        continue
    else:
        for i in range(2):
            nx = x + dx[i] * s
            ny = y + dy[i] * s
            if -1 < nx < n and -1 < ny < n and not visited[nx][ny]:
                d.append([nx, ny])
                visited[nx][ny]
if not ans:
    print("Hing")
