# https://www.acmicpc.net/problem/13549

from collections import deque

n, k = map(int, input().split())
if n >= k:
    print(n - k)
else:
    arr = [-1 for _ in range(100000 + 1)]

    d = []
    arr[n] = 0
    d += [n]
    while d:
        x = d[0]
        d = d[1:]
        if x == k:
            print(arr[k])
            break
        if x - 1 >= 0:
            if arr[x - 1] == -1:
                arr[x - 1] = arr[x] + 1
                d.append(x - 1)
            else:
                if arr[x - 1] > arr[x] + 1:
                    arr[x - 1] = arr[x] + 1
                    d.append(x - 1)

        if x + 1 <= 100000:
            if arr[x + 1] == -1:
                arr[x + 1] = arr[x] + 1
                d.append(x + 1)
            else:
                if arr[x + 1] > arr[x] + 1:
                    arr[x + 1] = arr[x] + 1
                    d.append(x + 1)
        if 2 * x <= 100000:
            if arr[x * 2] == -1:
                arr[x * 2] = arr[x]
                d = [x * 2] + d
            else:
                if arr[x * 2] > arr[x]:
                    arr[x * 2] = arr[x]
                    d = [x * 2] + d
