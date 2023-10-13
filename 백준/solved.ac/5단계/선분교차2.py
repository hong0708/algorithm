# https://www.acmicpc.net/problem/17387

import sys

x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
x3, y3, x4, y4 = map(int, sys.stdin.readline().split())


def ccw(x1, y1, x2, y2, x3, y3):
    tmp = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)
    tmp = (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)
    if tmp > 0:
        return 1
    elif tmp < 0:
        return -1
    else:
        return 0


answer = 0
flag = False

if ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4) == 0 and ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4,
                                                                                                        x2, y2) == 0:
    flag = True
    if min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(
            y1, y2):
        answer = 1
if ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4) <= 0 and ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4,
                                                                                                        x2, y2) <= 0:
    if not flag:
        answer = 1
print(answer)
