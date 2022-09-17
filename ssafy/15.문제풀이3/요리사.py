import itertools


def cook(food):
    result = 0
    for i in itertools.combinations(food, 2):
        i = list(i)
        result += data[i[0]][i[1]] + data[i[1]][i[0]]
    return result


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    cooks = [i for i in range(n)]
    data = [list(map(int, input().split())) for _ in range(n)]
    answer = 1000000

    for one in itertools.combinations(cooks, n // 2):
        one = list(one)
        two = []
        for j in cooks:
            if j not in one:
                two.append(j)
        p1 = cook(one)
        p2 = cook(two)
        if answer > abs(p1 - p2):
            answer = abs(p1 - p2)
    print("#{} {}".format(tc, answer))
