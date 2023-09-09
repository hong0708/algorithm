n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]
dist = [float('inf') for i in range(n + 1)]


def bf(start):
    dist[start] = 0
    for i in range(1, n + 1):  # 간선 탐색을 위한 for문. 간선이 n-1개여야 사이클 x.
        for a in range(1, n + 1):  # 노드 탐색을 위한 for문
            for next, time in graph[a]:
                if dist[a] != float('inf') and dist[next] > dist[a] + time:
                    dist[next] = dist[a] + time
                    if i == n:  # n-1번 이후에도 값이 갱신되면 음수 사이클 존재.
                        return True  # 사이클 존재.
    return False


for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    # dist[b] = c

negative_cycle = bf(1)
if negative_cycle:
    print(-1)
else:
    for i in range(2, n + 1):
        if dist[i] == float('inf'):
            print(-1)
        else:
            print(dist[i])
