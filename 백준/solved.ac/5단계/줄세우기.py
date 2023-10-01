# https://www.acmicpc.net/problem/2252

from collections import deque

n, m = map(int, input().split())
arr1 = [[] for _ in range(n + 1)]
arr2 = [[] for _ in range(n + 1)]
ans = []
for _ in range(m):
    s, e = map(int, input().split())
    arr1[s].append(e)
    arr2[e].append(s)

dq = deque()
visited = [False for _ in range(n + 1)]
for i in range(1, n + 1):
    if len(arr2[i]) == 0:
        dq.append(i)

while dq:
    now = dq.popleft()
    if not visited[now]:
        ans.append(now)
    for a in arr1[now]:
        dq.append(a)
print(*ans)
