# https://www.acmicpc.net/problem/2667

from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n = int(input())
arr = []
ans = [[0 for _ in range(n)] for _ in range(n)]

result = []

for _ in range(n):
    x = input()
    impl = []
    for i in x:
        impl.append(int(i))
    arr.append(impl)

num = 0


def find(a, b, r):
    d = deque()
    d.append([a, b])
    ans[a][b] = num
    res = 0
    while d:
        res += 1
        na, nb = d.pop()
        for i in range(4):
            nx = na + dx[i]
            ny = nb + dy[i]
            if -1 < nx < n and -1 < ny < n and arr[nx][ny] == 1 and ans[nx][ny] == 0:
                ans[nx][ny] = num
                d.append([nx, ny])
    r += [res]


for q in range(n):
    for w in range(n):
        if arr[q][w] == 1 and ans[q][w] == 0:
            num += 1
            find(q, w, result)

print(num)
result.sort()
for e in result:
    print(e)
