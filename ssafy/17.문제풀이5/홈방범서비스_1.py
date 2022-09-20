t = int(input())
for tc in range(1, t + 1):
    # n 한변의길이 m 한집이 지불하는 비용
    # 마름모는 가운데 점으로 부터 길이를 뜻함
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    idx = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                idx.append([i, j])

    max_cnt = 0
    for i in range(n):
        for j in range(n):
            for k in range(1, n + 2):
                home = 0
                for z in range(len(idx)):
                    if abs(i - idx[z][0]) + abs(j - idx[z][1]) <= k - 1:
                        home += 1
                if home * m >= k * k + (k - 1) * (k - 1):
                    max_cnt = max(max_cnt, home)
    print("#{} {}".format(tc, max_cnt))
