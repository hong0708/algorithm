# https://www.acmicpc.net/problem/25682

import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

arr_b = [[0 for _ in range(m)] for _ in range(n)]
p_b = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

arr_w = [[0 for _ in range(m)] for _ in range(n)]
p_w = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

arr = []

for _ in range(n):
    arr.append(input())

# B 시작
for i in range(n):
    for j in range(m):
        if i % 2 == 0 and j % 2 == 0:
            if arr[i][j] != 'B':
                arr_b[i][j] = 1
        elif i % 2 == 0 and j % 2 == 1:
            if arr[i][j] != 'W':
                arr_b[i][j] = 1
        elif i % 2 == 1 and j % 2 == 0:
            if arr[i][j] != 'W':
                arr_b[i][j] = 1
        else:
            if arr[i][j] != 'B':
                arr_b[i][j] = 1

# W 시작
for i in range(n):
    for j in range(m):
        if i % 2 == 0 and j % 2 == 0:
            if arr[i][j] != 'W':
                arr_w[i][j] = 1
        elif i % 2 == 0 and j % 2 == 1:
            if arr[i][j] != 'B':
                arr_w[i][j] = 1
        elif i % 2 == 1 and j % 2 == 0:
            if arr[i][j] != 'B':
                arr_w[i][j] = 1
        else:
            if arr[i][j] != 'W':
                arr_w[i][j] = 1

# 누적합 배열 만들기
for a in range(1, n + 1):
    for b in range(1, m + 1):
        p_b[a][b] = arr_b[a - 1][b - 1] + p_b[a - 1][b] + p_b[a][b - 1] - p_b[a - 1][b - 1]

for a in range(1, n + 1):
    for b in range(1, m + 1):
        p_w[a][b] = arr_w[a - 1][b - 1] + p_w[a - 1][b] + p_w[a][b - 1] - p_w[a - 1][b - 1]


min_arr = []

for i in range(k, n + 1):
    for j in range(k, m + 1):
        min_arr.append(p_b[i][j] - p_b[i - k][j] - p_b[i][j - k] + p_b[i - k][j - k])
        min_arr.append(p_w[i][j] - p_w[i - k][j] - p_w[i][j - k] + p_w[i - k][j - k])
print(min(min_arr))
