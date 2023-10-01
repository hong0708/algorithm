# https://www.acmicpc.net/problem/2252

from collections import deque

n, m = map(int, input().split())
line = [0 for _ in range(n + 1)]
arr1 = [[] for _ in range(n + 1)]
ans = []
for _ in range(m):
    s, e = map(int, input().split())
    arr1[s].append(e)
    line[e] += 1

dq = deque()

for i in range(1, n + 1):
    if line[i] == 0:
        dq.append(i)
while dq:
    now = dq.popleft()
    ans.append(now)
    for i in arr1[now]:
        line[i] -= 1
        if line[i] == 0:
            dq.append(i)
print(*ans)
