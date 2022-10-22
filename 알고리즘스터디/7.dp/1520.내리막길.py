dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def route(x, y):
    if x == n - 1 and y == m - 1:
        return 1
    if visited[x][y] != -1:
        return visited[x][y]
    visited[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if height[nx][ny] < height[x][y]:
                visited[x][y] += route(nx, ny)
    return visited[x][y]


n, m = map(int, input().split())
height = []
for _ in range(n):
    height.append(list(map(int, input().split())))
visited = [[-1 for _ in range(m)] for _ in range(n)]

print(route(0, 0))
