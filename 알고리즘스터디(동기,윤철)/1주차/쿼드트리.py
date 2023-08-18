# https://www.acmicpc.net/problem/1992

import sys

n = int(sys.stdin.readline())
arr = [list(sys.stdin.readline()) for _ in range(n)]
ans = ''


def slice(x, y, l):
    global ans
    now = arr[x][y]
    change = int(now)
    for i in range(x, x + l):
        for j in range(y, y + l):
            if now != arr[i][j]:
                change = -1
                break

    if change == -1:
        ans += '('
        slice(x, y, l // 2)
        slice(x, y + l // 2, l // 2)
        slice(x + l // 2, y, l // 2)
        slice(x + l // 2, y + l // 2, l // 2)
        ans += ')'

    elif change == 0:
        ans += '0'

    else:
        ans += '1'


slice(0, 0, n)
print(ans)
