dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def mapping(x, y):
    if x == n - 1 and y == m - 1:
        return 1

    if visited[x][y] == 1:
        return count[x][y]

    visited[x][y] = 1

    for i in range(4):
        tx = dx[i] + x
        ty = dy[i] + y
        if 0 <= tx < n and 0 <= ty < m:
            if mapp[tx][ty] < mapp[x][y]:
                count[x][y] += mapping(tx, ty)
    return count[x][y]

n, m = map(int, input().split())
mapp = []
for i in range(n):
    mapp.append(list(input().split()))
visited = [[0 for _ in range(m)] for _ in range(n)]
count = [[0] * m for _ in range(n)]
print(mapping(0, 0))
