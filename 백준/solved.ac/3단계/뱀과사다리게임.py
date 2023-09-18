# https://www.acmicpc.net/problem/16928

from collections import deque

n, m = map(int, input().split())
arr = [[] for _ in range(101)]
visited = [True, True] + [False for _ in range(99)]

for _ in range(n):
    x, y = map(int, input().split())
    arr[x].append(y)
for _ in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)

d = deque()
d.append([1, 0])

while d:
    now = d.popleft()
    l, w = now[0], now[1]
    if l == 100:
        print(w)
        break
    for i in range(1, 7):
        if l + i <= 100 and not visited[l + i]:
            visited[l + i] = True

            if len(arr[l + i]):
                d.append([arr[l + i][0], w + 1])
            else:
                d.append([l + i, w + 1])
