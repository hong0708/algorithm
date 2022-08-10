import random

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

data = [[0 for _ in range(5)] for _ in range(5)]
answer = 0
for i in range(5):
    for j in range(5):
        data[i][j] = int(random.randint(0, 100))

print(data)

for x in range(5):
    for y in range(5):
        addNum = 0
        orgNum = data[x][y]
        for z in range(4):
            if -1 < x + dx[z] < 4 and -1 < j + dy[z] < 4:
                addNum += abs(orgNum - data[x + dx[z]][y + dy[z]])
        answer += addNum
print(answer)