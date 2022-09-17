def cal_len(a, b, c, d):
    return ((a - b) ** 2 + (c - d) ** 2) ** (1 / 2)


INF = 1e8
t = int(input())
for tc in range(1, t + 1):
    answer = []
    n = int(input())
    data_x = list(map(int, input().split()))
    data_y = list(map(int, input().split()))
    e = float(input())
    idx = []
    for i in range(len(data_x)):
        idx.append([data_x[i], data_y[i]])

    num = len(idx)

    num_len = list([INF for _ in range(num)] for _ in range(num))

    for a in range(num):
        for b in range(num):
            num_len[a][b] = cal_len(idx[a][0], idx[b][0], idx[a][1], idx[b][1])

    count = num_len[0]
    visted = [False for _ in range(num)]
    visted[0] = True

    while False in visted:
        minLen = INF
        next_idx = 0
        for a in range(num):
            if visted[a] is False and minLen > count[a]:
                minLen = count[a]
                next_idx = a

        visted[next_idx] = True
        for a in range(num):
            if visted[a] is False:
                count[a] = min(count[a], num_len[next_idx][a])

    answer = 0
    for z in count:
        answer += e * z ** 2
    print("#{} {}".format(tc, round(answer)))
