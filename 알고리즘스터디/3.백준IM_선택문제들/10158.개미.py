dx = [-1, -1, 1, -1]
dy = [1, -1, -1, -1]
direction = 0

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

x = h - q
y = p
count = 0
print(p, q, x, y)
while True:
    if count == t:
        print(y, h - x)
        break

    if -1 < x + dx[direction] < h + 1 and -1 < y + dy[direction] < w + 1:
        x += dx[direction]
        y += dy[direction]
        count += 1

    else:
        if direction == 3:
            direction = 0
            x += dx[direction]
            y += dy[direction]
            count += 1
        else:
            direction += 1
            x += dx[direction]
            y += dy[direction]
            count += 1
