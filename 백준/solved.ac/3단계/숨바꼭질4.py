# https://www.acmicpc.net/problem/13913

from collections import deque

n, k = map(int, input().split())

arr = [-1 for _ in range(100000 + 1)]
move = [0 for _ in range(100000 + 1)]

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
            move[x - 1] = x
        else:
            if arr[x - 1] > arr[x] + 1:
                arr[x - 1] = arr[x] + 1
                d.append(x - 1)
                move[x - 1] = x

    if x + 1 <= 100000:
        if arr[x + 1] == -1:
            arr[x + 1] = arr[x] + 1
            d.append(x + 1)
            move[x + 1] = x
        else:
            if arr[x + 1] > arr[x] + 1:
                arr[x + 1] = arr[x] + 1
                d.append(x + 1)
                move[x + 1] = x
        if 2 * x <= 100000:
            if arr[x * 2] == -1:
                arr[x * 2] = arr[x] + 1
                d.append(x * 2)
                move[x * 2] = x
            else:
                if arr[x * 2] > arr[x] + 1:
                    arr[x * 2] = arr[x] + 1
                    d.append(x * 2)
                    move[x * 2] = x
ans = []
temp = k
for _ in range(arr[k] + 1):
    ans.append(temp)
    temp = move[temp]
ans.reverse()
print(*ans)
