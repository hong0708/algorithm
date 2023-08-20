# https://www.acmicpc.net/problem/18110

import heapq

n = int(input())


def r(a):
    if a - int(a) >= 0.5:
        return int(a) + 1
    else:
        return int(a)


if n:
    arr_min = []
    ans = 0
    c = r(n * 0.15)

    for i in range(n):
        x = int(input())
        heapq.heappush(arr_min, x)

    for i in range(c):
        heapq.heappop(arr_min)
    for i in range(n - 2 * c):
        x = heapq.heappop(arr_min)
        ans += int(x)
    print(r(ans / (n - 2 * c)))
else:
    print(0)
