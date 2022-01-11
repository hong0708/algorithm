from collections import deque


def cango(x_start, y_start):
    q, c = deque(), []
    q.append([x_start, y_start, 20])
    c.append([x_start, y_start, 20])
    while q:
        x, y, beer = q.popleft()
        if x == x_1 and y == y_1:
            print("happy")
            return

        for nx, ny in gs:
            if [nx, ny, 20] not in c:
                road = abs(nx - x) + abs(ny - y)
                if beer * 50 >= road:
                    q.append([nx, ny, 20])
                    c.append([nx, ny, 20])
    print("sad")
    return


t = int(input())

for _ in range(t):
    n = int(input())
    x_0, y_0 = map(int, input().split())

    gs = []
    for _ in range(n):
        x, y = map(int, input().split())
        gs.append([x, y])

    x_1, y_1 = map(int, input().split())
    gs.append([x_1, y_1])

    cango(x_0, y_0)
