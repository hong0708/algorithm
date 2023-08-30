# https://www.acmicpc.net/problem/12851

from collections import deque

n, k = map(int, input().split())
arr = [-1 for _ in range(100000 + 1)]

d = deque()
arr[n] = 0
d.append(n)

time = 0
count = 0

while d:
    x = d.popleft()

    if time != 0 and x == k and arr[x] == time:
        count += 1
    else:
        if x == k:
            time = arr[k]
            count += 1
        else:
            if x - 1 >= 0:
                if arr[x - 1] == -1:
                    arr[x - 1] = arr[x] + 1
                    d.append(x - 1)
                else:
                    if arr[x - 1] >= arr[x] + 1:
                        arr[x - 1] = arr[x] + 1
                        d.append(x - 1)

            if x + 1 <= 100000:
                if arr[x + 1] == -1:
                    arr[x + 1] = arr[x] + 1
                    d.append(x + 1)
                else:
                    if arr[x + 1] >= arr[x] + 1:
                        arr[x + 1] = arr[x] + 1
                        d.append(x + 1)
            if 2 * x <= 100000:
                if arr[x * 2] == -1:
                    arr[x * 2] = arr[x] + 1
                    d.append(x * 2)
                else:
                    if arr[x * 2] >= arr[x] + 1:
                        arr[x * 2] = arr[x] + 1
                        d.append(x * 2)
print(time)
print(count)
