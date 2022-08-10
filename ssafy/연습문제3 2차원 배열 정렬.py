data = [[9, 20, 2, 18, 11], [19, 1, 25, 3, 21], [8, 24, 10, 17, 7], [15, 3, 15, 5, 6], [12, 13, 22, 23, 14]]
dataNums = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
numbers = []
for i in range(25):
    numbers.append(i + 1)

direction = 0
x = 0
y = 0
while True:
    dataNums[x][y] = numbers[0]
    if len(numbers) != 1:
        del numbers[0]
    else: break

    if -1 < x + dx[direction] < 5 and -1 < y + dy[direction] < 5:
        if dataNums[x + dx[direction]][y + dy[direction]] == 0:
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
print(dataNums)
