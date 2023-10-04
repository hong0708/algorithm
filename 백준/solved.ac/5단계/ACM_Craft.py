# https://www.acmicpc.net/problem/1005

import sys
from collections import deque

for _ in range(int(input())):
    n, k = map(int, input().split())
    cost = [0] + list(map(int, sys.stdin.readline().split()))
    degree = [0 for _ in range(n + 1)]
    route = [[] for _ in range(n + 1)]
    res = [0 for _ in range(n + 1)]

    for _ in range(k):
        s, e = map(int, input().split())
        route[s].append(e)
        degree[e] += 1
    des = int(input())

    dq = deque()
    for i in range(1, n + 1):
        if degree[i] == 0:
            dq.append(i)
            res[i] = cost[i]

    while dq:
        now = dq.popleft()
        for next in route[now]:
            degree[next] -= 1
            res[next] = max(res[next], res[now] + cost[next])
            if degree[next] == 0:
                dq.append(next)

    print(res[des])
