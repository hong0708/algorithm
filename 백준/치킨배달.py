from itertools import combinations

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

house = []
chicken = []

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            house.append((i, j))
        elif board[i][j] == 2:
            chicken.append((i, j))

pick_chicken = list(combinations(chicken, M))
result = [0] * len(pick_chicken)

for i in house:
    for j in range(len(pick_chicken)):
        a = 101
        for k in pick_chicken[j]:
            temp = abs(i[0] - k[0]) + abs(i[1] - k[1])
            a = min(a, temp)
        result[j] += a

print(min(result))
