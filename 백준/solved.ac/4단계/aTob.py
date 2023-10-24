# https://www.acmicpc.net/problem/16953

import sys
from collections import deque

s, e = map(int, sys.stdin.readline().split())


def make(s, e):
    dq = deque()
    dq.append([s, 0])

    while dq:
        now = dq.popleft()
        n = now[0]
        cost = now[1]

        if n == e:
            return cost + 1
        if n > e:
            continue
        dq.append([n * 2, cost + 1])
        n = int(str(n) + '1')
        dq.append([n, cost + 1])

    return -1


print(make(s, e))
