# https://www.acmicpc.net/problem/9375

t = int(input())
for _ in range(t):
    n = int(input())

    count = []
    kind = []
    for _ in range(n):
        c, k = map(str, input().split())
        if k in kind:
            count[kind.index(k)] += 1
        else:
            kind.append(k)
            count.append(1)
    ans = 1

    for i in count:
        ans *= (i + 1)

    print(ans - 1)
