tc = int(input())
for t in range(tc):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    maxfly = 0
    for i in range(n):
        for j in range(n):
            count = 0
            for a in range(i, i + m):
                for b in range(j, j + m):
                    if a > n -1 or b > n-1:
                        break
                    else:
                        count += arr[a][b]
            if maxfly < count:
                maxfly = count

    print("#{} {}".format(t + 1, maxfly))
