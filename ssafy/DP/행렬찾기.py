def check_sq(x, y):
    w = 0
    h = 0
    for a in range(x, n):
        if data[a][y]:
            h += 1
        else:
            break
    for b in range(y, n):
        if data[x][b]:
            w += 1
        else:
            break

    for q in range(x, h + x):
        for p in range(y, w + y):
            visited[q][p] = True
    return [h, w, w * h]


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    data = list(list(map(int, input().split())) for _ in range(n))
    visited = [[False for _ in range(n)] for _ in range(n)]
    answer = []
    count = 0
    for i in range(n):
        for j in range(n):
            if data[i][j] != 0 and visited[i][j] == False:
                answer.append(check_sq(i, j))
                count += 1
    answer.sort(key=lambda x: (x[2], x[0]))

    print("#{} {}".format(tc, count, end=''))
    for r, c, _ in answer:
        print("{} {}".format(r, c), end=' ')
    print()