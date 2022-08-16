dataMap = list([-1 for _ in range(0, 101)] for _ in range(0, 101))
n = [0, 0, 0, 0]
answer = 0
for i in range(4):
    data = list(map(int, input().split()))
    for a in range(data[0], data[2], 1):
        for b in range(data[1], data[3], 1):
            if dataMap[a][b] == -1:
                dataMap[a][b] = i + 1
                answer += 1

print(answer)
