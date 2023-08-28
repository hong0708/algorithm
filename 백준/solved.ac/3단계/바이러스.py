# https://www.acmicpc.net/problem/2606

from collections import deque

n = int(input())
visited = [1] + [0 for _ in range(n - 1)]
c = int(input())
arr = []
for _ in range(c):
    x = list(map(int, input().split()))
    arr.append(x)

arr.sort(key=lambda x: x[0])

d = deque(arr)
count = 0
while count <= n and d:
    now = d.popleft()
    if visited[now[0] - 1]:
        visited[now[1] - 1] = 1
        count = 0
    elif visited[now[1] - 1]:
        visited[now[0] - 1] = 1
        count = 0
    else:
        d.append(now)
        count += 1

print(sum(visited) - 1)
