import itertools


def take(q, w, e, r):
    global max_hony
    result = 0
    hony = []

    for i in range(w, w + m):
        hony.append(data[q][i])
    if sum(hony) > c:
        if sum(hony) > c:
            hony = pick(hony)
    result += count_hony(hony)
    hony.clear()

    for j in range(r, r + m):
        hony.append(data[e][j])
    if sum(hony) > c:
        hony = pick(hony)
    result += count_hony(hony)

    if result > max_hony:
        max_hony = result


def count_hony(hony_list):
    money = 0
    for z in range(len(hony_list)):
        money += hony_list[z] ** 2
    return money


def pick(hony_list):
    result = []
    max_counting = 0
    for i in range(len(hony_list)):
        for j in itertools.combinations(hony_list, i):
            j = list(j)
            now = 0
            if sum(j) > c:
                continue
            else:
                for p in j:
                    now += p ** 2
            if max_counting < now:
                max_counting = now
                result = j
    return result


t = int(input())
for tc in range(1, t + 1):
    n, m, c = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]
    start = [i for i in range(n - m + 1)]
    max_hony = 0

    for a in range(n):
        for b in range(n):
            # 같은 라인에서 꿀
            if a == b:
                if n == 2 * m:
                    take(a, 0, b, m)
                elif n < 2 * m:
                    continue
                else:
                    for x in range(n - 2 * m):
                        for y in range(x + m, n - m):
                            take(a, x, b, y)
            else:
                if n == m:
                    take(a, 0, b, 0)
                else:
                    for x in range(0, n - m + 1):
                        for y in range(0, n - m + 1):
                            take(a, x, b, y)
    print("#{} {}".format(tc, max_hony))
