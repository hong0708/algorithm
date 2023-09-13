# https://www.acmicpc.net/problem/11279

import sys
import heapq

n = int(input())
hq = []

for _ in range(n):
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        if hq:
            print(heapq.heappop(hq) * -1)
        else:
            print(0)
    else:
        heapq.heappush(hq, -1 * x)

