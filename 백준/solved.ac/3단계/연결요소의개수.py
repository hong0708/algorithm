# https://www.acmicpc.net/problem/11724

from collections import deque

n, m = map(int, input().split())
arr = [[] for _ in range(n)]
ans = 0

for _ in range(m):
    x, y = map(int, input().split())
    arr[x - 1] += [y]
    arr[y - 1] += [x]

visited = [0 for _ in range(n)]

for i in range(n):
    if not visited[i]:
        d = deque([i])
        while d:
            now = d.pop()
            if not visited[now]:
                visited[now] = 1
                for a in arr[now]:
                    if not visited[a - 1]:
                        d.append(a - 1)

        ans += 1
print(ans)
