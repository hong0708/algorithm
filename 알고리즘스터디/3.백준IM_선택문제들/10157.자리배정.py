dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

c, r = map(int, input().split())
k = int(input())

data = list([0 for _ in range(c)] for _ in range(r))

count = 1

direction = 0
x = r - 1
y = 0
while True:
    if k > c * r:
        print(0)
        break
    if count == k:
        print(y + 1, r - x)
        break
    data[x][y] = count
    count += 1

    if -1 < x + dx[direction] < r and -1 < y + dy[direction] < c:
        if data[x + dx[direction]][y + dy[direction]] == 0:
            x += dx[direction]
            y += dy[direction]

        else:
            if direction == 3:
                direction = 0
                x += dx[direction]
                y += dy[direction]
            else:
                direction += 1
                x += dx[direction]
                y += dy[direction]

    else:
        if direction == 3:
            direction = 0
            x += dx[direction]
            y += dy[direction]
        else:
            direction += 1
            x += dx[direction]
            y += dy[direction]
