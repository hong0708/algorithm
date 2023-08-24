# https://www.acmicpc.net/problem/1927

import heapq
import sys

n = int(input())
arr = []

for i in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if arr:
            print(heapq.heappop(arr))
        else:
            print(0)
    else:
        heapq.heappush(arr, x)
