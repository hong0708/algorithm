# https://www.acmicpc.net/problem/15683

from collections import deque
from copy import deepcopy

n, m = map(int, input().split())
arr = []
ans = n * m

# cctv 종류,x,y
cctv = []

for i in range(n):
    impl = list(map(int, input().split()))
    if sum(impl) > 0:
        for j in range(m):
            if impl[j] in [1, 2, 3, 4, 5]:
                cctv.append([impl[j], i, j])
    arr.append(impl)


def check(kind, d, vi, x, y):
    now = deepcopy(vi)
    if kind == 1:
        if d == 0:
            for i in range(y, m):
                if now[x][i] == 6:
                    break
                elif now[x][i] == 0:
                    now[x][i] = '#'
                else:
                    continue
        elif d == 1:
            for i in range(x, n):
                if now[i][y] == 6:
                    break
                elif now[i][y] == 0:
                    now[i][y] = '#'
                else:
                    continue
        elif d == 2:
            for i in range(y, -1, -1):
                if now[x][i] == 6:
                    break
                elif now[x][i] == 0:
                    now[x][i] = '#'
                else:
                    continue
        else:
            for i in range(x, -1, -1):
                if now[i][y] == 6:
                    break
                elif now[i][y] == 0:
                    now[i][y] = '#'
                else:
                    continue
    elif kind == 2:
        if d == 0:
            for i in range(y, m):
                if now[x][i] == 6:
                    break
                elif now[x][i] == 0:
                    now[x][i] = '#'
                else:
                    continue
            for i in range(y, -1, -1):
                if now[x][i] == 6:
                    break
                elif now[x][i] == 0:
                    now[x][i] = '#'
                else:
                    continue
        elif d == 1:
            for i in range(x, -1, -1):
                if now[i][y] == 6:
                    break
                elif now[i][y] == 0:
                    now[i][y] = '#'
                else:
                    continue
            for i in range(x, n):
                if now[i][y] == 6:
                    break
                elif now[i][y] == 0:
                    now[i][y] = '#'
                else:
                    continue
    elif kind == 3:
        if d == 0:
            for i in range(x, -1, -1):
                if now[i][y] == 6:
                    break
                elif now[i][y] == 0:
                    now[i][y] = '#'
                else:
                    continue
            for i in range(y, m):
                if now[x][i] == 6:
                    break
                elif now[x][i] == 0:
                    now[x][i] = '#'
                else:
                    continue
        elif d == 1:
            for i in range(y, m):
                if now[x][i] == 6:
                    break
                elif now[x][i] == 0:
                    now[x][i] = '#'
                else:
                    continue
            for i in range(x, n):
                if now[i][y] == 6:
                    break
                elif now[i][y] == 0:
                    now[i][y] = '#'
                else:
                    continue
        elif d == 2:
            for i in range(x, n):
                if now[i][y] == 6:
                    break
                elif now[i][y] == 0:
                    now[i][y] = '#'
                else:
                    continue
            for i in range(y, -1, -1):
                if now[x][i] == 6:
                    break
                elif now[x][i] == 0:
                    now[x][i] = '#'
                else:
                    continue
        elif d == 3:
            for i in range(y, -1, -1):
                if now[x][i] == 6:
                    break
                elif now[x][i] == 0:
                    now[x][i] = '#'
                else:
                    continue
            for i in range(x, -1, -1):
                if now[i][y] == 6:
                    break
                elif now[i][y] == 0:
                    now[i][y] = '#'
                else:
                    continue
    elif kind == 4:
        if d == 0:
            for i in range(y, m):
                if now[x][i] == 6:
                    break
                elif now[x][i] == 0:
                    now[x][i] = '#'
                else:
                    continue
            for i in range(y, -1, -1):
                if now[x][i] == 6:
                    break
                elif now[x][i] == 0:
                    now[x][i] = '#'
                else:
                    continue
            for i in range(x, -1, -1):
                if now[i][y] == 6:
                    break
                elif now[i][y] == 0:
                    now[i][y] = '#'
                else:
                    continue
        elif d == 1:
            for i in range(y, m):
                if now[x][i] == 6:
                    break
                elif now[x][i] == 0:
                    now[x][i] = '#'
                else:
                    continue
            for i in range(x, -1, -1):
                if now[i][y] == 6:
                    break
                elif now[i][y] == 0:
                    now[i][y] = '#'
                else:
                    continue
            for i in range(x, n):
                if now[i][y] == 6:
                    break
                elif now[i][y] == 0:
                    now[i][y] = '#'
                else:
                    continue
        elif d == 2:
            for i in range(y, m):
                if now[x][i] == 6:
                    break
                elif now[x][i] == 0:
                    now[x][i] = '#'
                else:
                    continue
            for i in range(y, -1, -1):
                if now[x][i] == 6:
                    break
                elif now[x][i] == 0:
                    now[x][i] = '#'
                else:
                    continue
            for i in range(x, n):
                if now[i][y] == 6:
                    break
                elif now[i][y] == 0:
                    now[i][y] = '#'
                else:
                    continue
        elif d == 3:
            for i in range(x, -1, -1):
                if now[i][y] == 6:
                    break
                elif now[i][y] == 0:
                    now[i][y] = '#'
                else:
                    continue
            for i in range(x, n):
                if now[i][y] == 6:
                    break
                elif now[i][y] == 0:
                    now[i][y] = '#'
                else:
                    continue
            for i in range(y, -1, -1):
                if now[x][i] == 6:
                    break
                elif now[x][i] == 0:
                    now[x][i] = '#'
                else:
                    continue
    else:
        for i in range(y, m):
            if now[x][i] == 6:
                break
            elif now[x][i] == 0:
                now[x][i] = '#'
            else:
                continue
        for i in range(y, -1, -1):
            if now[x][i] == 6:
                break
            elif now[x][i] == 0:
                now[x][i] = '#'
            else:
                continue
        for i in range(x, -1, -1):
            if now[i][y] == 6:
                break
            elif now[i][y] == 0:
                now[i][y] = '#'
            else:
                continue
        for i in range(x, n):
            if now[i][y] == 6:
                break
            elif now[i][y] == 0:
                now[i][y] = '#'
            else:
                continue

    return now


def count(res):
    count = 0
    for i in range(n):
        for j in range(m):
            if res[i][j] == 0:
                count += 1
    return count


def b(loc, vi):
    global ans
    if cctv[loc][0] == 1:
        for i in range(4):
            res = check(1, i, vi, cctv[loc][1], cctv[loc][2])
            if loc == len(cctv) - 1:
                ans = min(ans, count(res))
            else:
                b(loc + 1, res)

    elif cctv[loc][0] == 2:
        for i in range(2):
            res = check(2, i, vi, cctv[loc][1], cctv[loc][2])
            if loc == len(cctv) - 1:
                ans = min(ans, count(res))
            else:
                b(loc + 1, res)

    elif cctv[loc][0] == 3:
        for i in range(4):
            res = check(3, i, vi, cctv[loc][1], cctv[loc][2])
            if loc == len(cctv) - 1:
                ans = min(ans, count(res))
            else:
                b(loc + 1, res)

    elif cctv[loc][0] == 4:
        for i in range(4):
            res = check(4, i, vi, cctv[loc][1], cctv[loc][2])
            if loc == len(cctv) - 1:
                ans = min(ans, count(res))
            else:
                b(loc + 1, res)

    elif cctv[loc][0] == 5:
        res = check(5, 0, vi, cctv[loc][1], cctv[loc][2])
        if loc == len(cctv) - 1:
            ans = min(ans, count(res))
        else:
            b(loc + 1, res)


if cctv:
    b(0, arr)
else:
    ans = count(arr)
print(ans)
