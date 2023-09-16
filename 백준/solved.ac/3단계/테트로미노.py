# https://www.acmicpc.net/problem/14500

import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
arr = []
for _ in range(n):
    impl = list(map(int, sys.stdin.readline().rstrip().split()))
    arr.append(impl)


def a(x, y):
    res = 0
    if y < m - 3:
        l = 0
        for k in range(y, y + 4):
            l += arr[x][k]
        res = max(res, l)
    if x < n - 3:
        l = 0
        for k in range(x, x + 4):
            l += arr[k][y]
        res = max(res, l)
    return res


def b(x, y):
    res = 0
    if x < n - 2 and y < m - 1:
        res = max(res, arr[x][y] + arr[x + 1][y] + arr[x + 2][y] + arr[x + 2][y + 1])
    if x < n - 2 and 0 < y:
        res = max(res, arr[x][y] + arr[x + 1][y] + arr[x + 2][y] + arr[x + 2][y - 1])
    if 0 < x and y < m - 2:
        res = max(res, arr[x][y] + arr[x][y + 1] + arr[x][y + 2] + arr[x - 1][y + 2])
    if x < n - 1 and y < m - 2:
        res = max(res, arr[x][y] + arr[x][y + 1] + arr[x][y + 2] + arr[x + 1][y + 2])
    if 0 < x and y < m - 2:
        res = max(res, arr[x][y] + arr[x - 1][y + 1] + arr[x - 1][y + 2] + arr[x - 1][y])
    if x < n - 1 and y < m - 2:
        res = max(res, arr[x][y] + arr[x + 1][y + 1] + arr[x + 1][y + 2] + arr[x + 1][y])
    if x < n - 2 and y < m - 1:
        res = max(res, arr[x][y] + arr[x][y + 1] + arr[x + 1][y + 1] + arr[x + 2][y + 1])
    if x < n - 2 and 0 < y:
        res = max(res, arr[x][y] + arr[x][y - 1] + arr[x + 1][y - 1] + arr[x + 2][y - 1])
    return res


def c(x, y):
    res = 0
    if x < n - 2 and y < m - 1:
        res = max(res, arr[x][y] + arr[x + 1][y] + arr[x + 1][y + 1] + arr[x + 2][y + 1])
    if x < n - 2 and 0 < y:
        res = max(res, arr[x][y] + arr[x + 1][y] + arr[x + 1][y - 1] + arr[x + 2][y - 1])
    if x < n - 1 and y < m - 2:
        res = max(res, arr[x][y] + arr[x][y + 1] + arr[x + 1][y + 1] + arr[x + 1][y + 2])
    if 0 < x and y < m - 2:
        res = max(res, arr[x][y] + arr[x][y + 1] + arr[x - 1][y + 1] + arr[x - 1][y + 2])

    return res


def d(x, y):
    res = 0
    if x < n - 1 and y < m - 2:
        res = max(res, arr[x][y] + arr[x + 1][y + 1] + arr[x][y + 1] + arr[x][y + 2])
    if 0 < x and y < m - 2:
        res = max(res, arr[x][y] + arr[x - 1][y + 1] + arr[x][y + 2] + arr[x][y + 1])
    if x < n - 2 and y < m - 1:
        res = max(res, arr[x][y] + arr[x + 1][y + 1] + arr[x + 1][y] + arr[x + 2][y])
    if x < n - 2 and 0 < y:
        res = max(res, arr[x][y] + arr[x + 1][y] + arr[x + 1][y - 1] + arr[x + 2][y])
    return res


ans = 0
for i in range(n):
    for j in range(m):
        if j < m - 1 and i < n - 1:
            ans = max(ans, arr[i][j] + arr[i + 1][j] + arr[i][j + 1] + arr[i + 1][j + 1])
        ans = max(a(i, j), ans)
        ans = max(b(i, j), ans)
        ans = max(c(i, j), ans)
        ans = max(d(i, j), ans)
print(ans)
