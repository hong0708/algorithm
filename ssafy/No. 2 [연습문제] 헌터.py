from collections import deque
import itertools
import copy


def countRoute(a):
    global minCount
    nowCount = locs[a[0]][0] + locs[a[0]][1]

    for i in range(len(a) - 1):
        nowCount += abs(locs[a[i]][0] - locs[a[i + 1]][0])
        nowCount += abs(locs[a[i]][1] - locs[a[i + 1]][1])

    if minCount > nowCount:
        minCount = nowCount


t = int(input())
for tc in range(t):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    minCount = 100000

    monCount = 0

    for a in range(n):
        for b in range(n):
            if data[a][b] != 0:
                monCount += 1

    locs = [[-1, -1] for _ in range(monCount + 1)]
    for a in range(n):
        for b in range(n):
            # m 위치
            if data[a][b] > 0:
                locs[data[a][b]][0] = a
                locs[data[a][b]][1] = b
            # p 위치
            elif data[a][b] < 0:
                locs[-1 * data[a][b] + (monCount // 2)][0] = a
                locs[-1 * data[a][b] + (monCount // 2)][1] = b

    # print(locs)
    mon = []
    people = []
    turn = []

    for i in range(monCount // 2):
        mon.append(i + 1)
        people.append(i + 1 + monCount // 2)
        turn.append(i + 1)
        turn.append(i + 1 + monCount // 2)

    # print(people, mon, turn)

    for i in itertools.permutations(turn, len(turn)):
        a = list(i)
        wrong = False
        for j in range(len(turn) // 2):
            if a.index(mon[j]) > a.index(people[j]):
                wrong = True
                break
        if wrong == False:
            # print(a)
            countRoute(a)

    print("#{} {}".format(tc + 1, minCount))
