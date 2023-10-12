# https://www.acmicpc.net/problem/20040

n, m = map(int, input().split())
parent = [i for i in range(n)]
ans = 0


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


for i in range(1, m + 1):
    s, e = map(int, input().split())

    a = find(s)
    b = find(e)
    if a == b:
        ans = i
        break
    else:
        union(a, b)

print(ans)
