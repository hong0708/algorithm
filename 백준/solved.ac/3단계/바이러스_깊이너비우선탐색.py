# https://www.acmicpc.net/problem/2606

from collections import deque

n = int(input())
visited = [0 for _ in range(n)]
c = int(input())
arr = [[] for _ in range(n)]

for _ in range(c):
    x, y = map(int, input().split())
    arr[x - 1] += [y]
    arr[y - 1] += [x]

d = deque([1])
while d:
    now = d.pop()
    for i in arr[now - 1]:
        if visited[i - 1] == 0:
            d.append(i)
            visited[i - 1] = 1
if visited[0] == 0:
    print(0)
else:
    print(sum(visited) - 1)
