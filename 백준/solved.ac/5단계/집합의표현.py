# https://www.acmicpc.net/problem/1717

import sys

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]


def find(x):
    while x != parent[x]:
        x = parent[x]
    return x


for _ in range(m):
    k, a, b = map(int, sys.stdin.readline().split())
    if k == 0:
        x = find(a)
        y = find(b)

        if x > y:
            parent[y] = x
        else:
            parent[x] = y
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
