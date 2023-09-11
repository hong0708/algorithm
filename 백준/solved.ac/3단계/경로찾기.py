# https://www.acmicpc.net/problem/11403

n = int(input())
arr = []
INF = 1e9

for i in range(n):
    impl = list(map(int, input().split()))
    for j in range(n):
        if impl[j] == 0:
            impl[j] = INF
    arr.append(impl)

for i in range(n):  # 중간점 즉 거치는 점을 순차적으로 한다
    for j in range(n):  # 시작점
        for k in range(n):  # 끝점
            if arr[j][k] > arr[j][i] + arr[i][k]:
                arr[j][k] = arr[j][i] + arr[i][k]

for a in range(n):
    for b in range(n):
        if arr[a][b] == INF:
            arr[a][b] = 0
        else:
            arr[a][b] = 1
    print(*arr[a])
