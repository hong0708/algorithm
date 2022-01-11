from collections import deque

N = int(input())
graph = [[] for _ in range(N + 1)]
min_score = 51
candidate = []

while True:
    p1, p2 = map(int, input().split())
    if p1 == -1 and p2 == -1:
        break
    graph[p1].append(p2)
    graph[p2].append(p1)


def BFS(i, graph):
    global min_score, candidate
    visited = [0] * (N + 1)
    Q = deque()
    Q.append(i)
    visited[i] = 1
    while Q:
        v = Q.popleft()
        for node in graph[v]:
            if visited[node] == 0:
                visited[node] = visited[v] + 1
                Q.append(node)
        if len(Q) == 0:
            score = visited[v] - 1

            if min_score > score:
                min_score = score
                candidate = [i]
            elif min_score == score:
                candidate.append(i)


for i in range(1, N + 1):
    BFS(i, graph)

print(min_score, len(candidate))
# *하고 배열하면 [] 사라지고 1 2 3 4 이런식으로 나온다
print(*candidate)
