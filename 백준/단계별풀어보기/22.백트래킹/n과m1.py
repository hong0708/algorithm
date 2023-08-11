# https://www.acmicpc.net/problem/15649

N, M = map(int, input().split())
arr = []


def back(a, n, m):
    if len(a) == m:
        print(*a)
    for i in range(1, n + 1):
        if i not in a:
            a = a + [i]
            back(a, n, m)
            a = a[:-1]


back(arr, N, M)
