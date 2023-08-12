# https://www.acmicpc.net/problem/15652

N, M = map(int, input().split())
arr = []


def back(a, n, m, now):
    if len(a) == m:
        print(*a)
    else:
        for i in range(now, n + 1):
            a = a + [i]
            back(a, n, m, i)
            a = a[:-1]


back(arr, N, M, 1)
