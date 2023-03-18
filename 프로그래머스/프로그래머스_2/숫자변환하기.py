INF = 100000


def solution(x, y, n):
    impl = [INF for _ in range(y + 1)]
    impl[x] = 0
    if x == y:
        return 0

    for i in range(x, y + 1):
        if impl[i] == INF:
            continue
        if i + n <= y:
            impl[i + n] = min(impl[i + n], impl[i] + 1)

        if i * 2 <= y:
            impl[i * 2] = min(impl[i * 2], impl[i] + 1)

        if i * 3 <= y:
            impl[i * 3] = min(impl[i * 3], impl[i] + 1)

    if impl[y] >= INF:
        return -1
    else:
        return impl[y]


print(solution(10, 40, 30))
