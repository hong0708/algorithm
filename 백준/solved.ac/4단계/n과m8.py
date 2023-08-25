# https://www.acmicpc.net/problem/15657

n, m = map(int, input().split())
arr = list(map(int, input().split()))
ans = []
arr.sort()


def b(a, loc):
    if len(a) == m:
        print(*a)
    else:
        for i in range(loc, n):
            a.append(arr[i])
            b(a, i)
            a.pop()


b(ans, 0)
