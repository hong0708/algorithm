# https://www.acmicpc.net/problem/1697

from collections import deque

n, k = map(int, input().split())
if n >= k:
    print(n - k)
else:
    arr = [-1 for _ in range(100000 + 10)]

    d = deque()
    arr[n] = 0
    d.append(n)
    while d:
        x = d.popleft()
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

        if x + 1 <= 100002:
            if arr[x + 1] == -1:
                arr[x + 1] = arr[x] + 1
                d.append(x + 1)
            else:
                if arr[x + 1] > arr[x] + 1:
                    arr[x + 1] = arr[x] + 1
                    d.append(x + 1)
        if 2 * x <= 100002:
            if arr[x * 2] == -1:
                arr[x * 2] = arr[x] + 1
                d.append(x * 2)
            else:
                if arr[x * 2] > arr[x] + 1:
                    arr[x * 2] = arr[x] + 1
                    d.append(x * 2)
