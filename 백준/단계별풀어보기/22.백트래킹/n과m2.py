# https://www.acmicpc.net/problem/15650

N, M = map(int, input().split())
arr = []


def back(a, n, m, now):
    if len(a) == m:
        print(*a)
    for i in range(now, n + 1):
        if i not in a:
            a = a + [i]
            back(a, n, m, i)
            a = a[:-1]


back(arr, N, M, 1)
