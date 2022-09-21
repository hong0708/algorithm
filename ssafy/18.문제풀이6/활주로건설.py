import copy


def make(z):
    global answer
    global count
    road = z.copy()
    r = len(road)
    visited = [False for _ in range(n)]
    if road in answer:
        count += 1
        answer.append(road)
    else:
        if len(set(road)) == 1:
            count += 1
            answer.append(road)
            return

        can = True
        for q in range(r - 1):

            # 1차이가 아닌경우
            if abs(road[q] - road[q + 1]) > 1:
                return

            # 1차이로 내려가는 경우
            elif road[q] - road[q + 1] == 1:
                # 길이가 x 까지 깔 수 있는지
                if q + x < n:
                    now = road[q + 1]
                    # x 길이 만큼 평평한지
                    for p in range(1, x + 1):
                        if road[q + p] != now or visited[q + p]:
                            can = False
                            return
                        visited[q + p] = True
                else:
                    can = False
                    return

            # 1차이로 올라가는 경우
            elif road[q] - road[q + 1] == -1:
                # 길이가 x 까지 깔 수 있는지
                if q - x + 1 >= 0:
                    now = road[q]
                    # x 길이 만큼 평평한지
                    for p in range(0, x):
                        if road[q - p] != now or visited[q - p]:
                            can = False
                            return
                        visited[q - p] = True
                else:
                    can = False
                    return
        if can:
            count += 1
            answer.append(road)
            return


t = int(input())
for tc in range(1, t + 1):
    # x 발판 길이
    n, x = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]
    answer = []
    count = 0

    case = []
    for i in range(n):
        w = []
        h = []
        for j in range(n):
            w.append(data[i][j])
            h.append(data[j][i])
        case.append(w)
        case.append(h)

    for a in range(len(case)):
        make(case[a])
    print("#{} {}".format(tc, count))
