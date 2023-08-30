# https://www.acmicpc.net/problem/1620

n, m = map(int, input().split())
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
d = {}

for i in range(1, n + 1):
    a = input()
    d[i] = a
    d[a] = i

for i in range(m):
    q = input()

    if q.isdigit():
        print(d[int(q)])
    else:
        print(d[q])
