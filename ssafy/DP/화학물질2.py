def make(start_x, start_y, start_left):
    global answer
    global ans
    x = start_x
    y = start_y
    add(x, y)
    can = True
    while can:
        for a in range(len(start_left)):
            if y == start_left[a][0]:
                x = start_left[a][0]
                y = start_left[a][1]
                add(x, y)
                can = True
                break
            can = False
    if len(answer) > len(ans):
        ans = answer
        answer = []
    else:
        answer = []


def add(start, end):
    global answer
    answer.append([start, end])


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
    return [h, w]


def find_min(start, end):
    global min_matrix, ans

    if start == end:
        return 0
    else:
        result = ans[start][0] * ans[end][0] * ans[end][1]

        if min_matrix[start][end] != 0:
            return min_matrix[start][end]

        elif start + 1 == end:
            min_matrix[start][end] = result
            return result

        else:
            get = min([find_min(start, z) + find_min(z + 1, end) + ans[start][0] * ans[end][1] * ans[z][1] for z in
                       range(start, end)])
            min_matrix[start][end] = get
            return get


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    data = list(list(map(int, input().split())) for _ in range(n))
    visited = [[False for _ in range(n)] for _ in range(n)]
    m_list = []
    answer = []
    ans = []

    for i in range(n):
        for j in range(n):
            if data[i][j] != 0 and visited[i][j] == False:
                m_list.append(check_sq(i, j))

    m_list.sort(key=lambda x: x[0])

    for i in range(len(m_list)):
        left = m_list.copy()
        left.pop(i)
        make(m_list[i][0], m_list[i][1], left)

    min_matrix = [[0 for _ in range(len(ans))] for _ in range(len(ans))]
    count = find_min(0, len(ans) - 1)

    print("#{} {}".format(tc, count))
