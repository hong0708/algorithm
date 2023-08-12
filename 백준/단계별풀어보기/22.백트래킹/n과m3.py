# https://www.acmicpc.net/problem/15651

N, M = map(int, input().split())
arr = []


def back(a, n, m):
    if len(a) == m:
        print(*a)
    else:
        for i in range(1, n + 1):
            a = a + [i]
            back(a, n, m)
            a = a[:-1]


back(arr, N, M)
