# https://www.acmicpc.net/problem/11779

import sys
import heapq
from collections import deque

INF = 1e9
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
arr = [[] for _ in range(n + 1)]
ans = [INF for _ in range(n + 1)]
road = [0 for _ in range(n + 1)]

for _ in range(m):
    s, e, w = map(int, sys.stdin.readline().split())
    arr[s].append([e, w])

start, end = map(int, sys.stdin.readline().split())
hq = [[start, 0]]
road[start] = 0

while hq:
    now = heapq.heappop(hq)
    x, w = now[0], now[1]
    # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
    # 즉 현재 가중치가 이미 답으로 나온 가중치보다 크다면 처리 완료된 노드임
    if w > ans[x]:
        continue
    for i in arr[x]:
        if ans[i[0]] > w + i[1]:
            ans[i[0]] = w + i[1]
            road[i[0]] = x
            heapq.heappush(hq, [i[0], w + i[1]])
print(ans[end])

# 경로를 저장하기엔 너무 크기때문에 이전에 어디 지점에서 왔는지 적어서 역추적해야함
result = []
dq = deque()
dq.append(end)
while dq:
    now = dq.pop()
    result.append(now)
    if now == start:
        break
    dq.append(road[now])
print(len(result))
print(*result[::-1])
