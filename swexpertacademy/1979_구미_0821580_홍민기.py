tc = int(input())
for t in range(tc):
    answer = 0
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        words = 0
        for j in range(n):
            if arr[j][i] == 1:
                words += 1
            if j == n - 1 or arr[j][i] == 0:
                if words == k:
                    answer += 1
                words = 0
        for z in range(n):
            if arr[i][z] == 1:
                words += 1
            if z == n - 1 or arr[i][z] == 0:
                if words == k:
                    answer += 1
                words = 0
    print("#{} {}".format(t+1, answer))
