# https://www.acmicpc.net/problem/27172

import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
visited = [False for _ in range(max(arr) + 1)]
ans = [0 for _ in range(len(visited))]
res = []
for num in arr:
    visited[num] = True

for a in range(n):
    for b in range(arr[a] * 2, len(visited), arr[a]):
        if visited[b]:
            ans[arr[a]] += 1
            ans[b] -= 1
for i in range(n):
    res.append(ans[arr[i]])
print(*res)
