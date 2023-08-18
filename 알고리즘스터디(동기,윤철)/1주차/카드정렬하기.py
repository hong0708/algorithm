# https://www.acmicpc.net/problem/1715

import heapq

n = int(input())
arr = []
ans = 0

for i in range(n):
    heapq.heappush(arr, int(input()))

while arr:
    if len(arr) == 1:
        break
    elif len(arr) == 2:
        a = heapq.heappop(arr)
        b = heapq.heappop(arr)
        ans += a + b
    else:
        a = heapq.heappop(arr)
        b = heapq.heappop(arr)
        ans += a + b
        heapq.heappush(arr, a + b)

print(ans)
