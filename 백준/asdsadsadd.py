n, m = map(int, input().split())
maplist = [input() for _ in range(n)]

check = min(n, m)
answer = 0
for i in range(n):
    for j in range(m):
        for k in range(check):
            if ((i + k) < n) and ((j + k) < m) and (maplist[i][j] == maplist[i][j + k] == maplist[i + k][j] == maplist[i + k][j + k]):
                answer = max(answer, (k + 1)**2)
print (answer)