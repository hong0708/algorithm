t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    data = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)
    count = 0

    for i in range(m):
        a, b = map(int, input().split())
        data[a].append(b)
        data[b].append(a)

    for node in range(1, n + 1):
        if not visited[node]:
            visited[node] = 1
            count += 1
            stack = [node]
            while stack:
                now = stack.pop()
                for nxt in data[now]:
                    if not visited[nxt]:
                        visited[nxt] = 1
                        stack.append(nxt)

    print('#{} {}'.format(tc, count))
