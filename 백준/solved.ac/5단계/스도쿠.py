# https://www.acmicpc.net/problem/2239

from copy import deepcopy

matrix = []
# 행 / 열 / 네모
arr = [[[False for _ in range(9)] for _ in range(9)], [[False for _ in range(9)] for _ in range(9)],
       [[False for _ in range(9)] for _ in range(9)]]
z = 0
res = [[0 for _ in range(9)] for _ in range(9)]

for i in range(9):
    a = list(map(int, input()))
    for j in range(9):
        if a[j]:
            arr[0][i][a[j] - 1] = True
            arr[1][j][a[j] - 1] = True
    for j in range(9):
        if a[j]:
            arr[2][(i // 3) * 3 + j // 3][a[j] - 1] = True

    matrix.append(a)
    z += a.count(0)


def find(cz):
    global res

    if cz == 0:
        if res[8][8] == 0:
            res = deepcopy(matrix)
        else:
            if res[8][8] > matrix[8][8]:
                res = deepcopy(matrix)

    for i in range(9):
        for j in range(9):
            if matrix[i][j] == 0:
                for x in range(1, 10):
                    if not arr[0][i][x - 1] and not arr[1][j][x - 1] and not arr[2][(i // 3) * 3 + j // 3][x - 1]:
                        matrix[i][j] = x
                        arr[0][i][x - 1], arr[1][j][x - 1], arr[2][(i // 3) * 3 + j // 3][x - 1] = True, True, True
                        find(cz - 1)
                        matrix[i][j] = 0
                        arr[0][i][x - 1], arr[1][j][x - 1], arr[2][(i // 3) * 3 + j // 3][x - 1] = False, False, False
                return


find(z)
for i in range(9):
    print(*res[i])
