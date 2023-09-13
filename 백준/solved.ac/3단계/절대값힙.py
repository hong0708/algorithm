# https://www.acmicpc.net/problem/11286

import sys
import heapq

n = int(input())
hq = []

for _ in range(n):
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        if hq:
            now, pm = heapq.heappop(hq)
            print(pm * now)
        else:
            print(0)
    elif x > 0:
        heapq.heappush(hq, (x, 1))
    else:
        heapq.heappush(hq, (-1 * x, -1))
