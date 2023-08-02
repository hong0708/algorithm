# https://www.acmicpc.net/problem/11660

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for i in range(n):
    impl = list(map(int, input().split()))
    arr.append(impl)
p = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

# 누적합 배열 만들기
for a in range(1, n + 1):
    for b in range(1, n + 1):
        p[a][b] = arr[a - 1][b - 1] + p[a - 1][b] + p[a][b - 1] - p[a - 1][b - 1]

for j in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(p[x2][y2] - p[x1 - 1][y2] - p[x2][y1 - 1] + p[x1 - 1][y1 - 1])
