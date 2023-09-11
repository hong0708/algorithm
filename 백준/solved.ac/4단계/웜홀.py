# https://www.acmicpc.net/problem/1865

INF = 10001


def b(start, na, arr):
    ans = [INF for _ in range(na + 1)]
    ans[start] = 0

    for a in range(1, na + 1):
        for b in range(1, na + 1):
            for next, w in arr[b]:
                if ans[next] > ans[b] + w:
                    ans[next] = ans[b] + w
                    if a == na:
                        return True
    return False


tc = int(input())
for _ in range(tc):
    n, m, w = map(int, input().split())
    r = [[] for _ in range(n + 1)]

    for _ in range(m):
        s, e, t = map(int, input().split())
        r[s].append([e, t])
        r[e].append([s, t])
    for _ in range(w):
        s, e, t = map(int, input().split())
        r[s].append([e, -t])

    # for i in range(1, n + 1):
    is_cycle = b(1, n, r)
    if not is_cycle:
        print('NO')

    if is_cycle:
        print('YES')
