# https://www.acmicpc.net/problem/14938

from collections import deque

INF = 1e9
n, m, r = map(int, input().split())
item = [0] + list(map(int, input().split()))
arr = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
ans = 0

for i in range(1, r + 1):
    s, e, w = map(int, input().split())
    arr[s][e] = w
    arr[e][s] = w

for i in range(1, n + 1):
    arr[i][i] = 0

for x in range(1, n + 1):
    for y in range(1, n + 1):
        for z in range(1, n + 1):
            if arr[y][z] > arr[y][x] + arr[x][z]:
                arr[y][z] = arr[y][x] + arr[x][z]

for i in range(1, n + 1):
    impl = 0
    for j in range(1, n + 1):
        if arr[i][j] <= m:
            impl += item[j]
    ans = max(ans, impl)
print(ans)
