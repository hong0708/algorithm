# https://www.acmicpc.net/problem/1021
from collections import deque

n, m = map(int, input().split())
loc = list(map(int, input().split()))
d = deque([i for i in range(1, n + 1)])
ans = 0

for i in range(m):
    while True:
        if d[0] == loc[i]:
            d.popleft()
            break
        else:
            if d.index(loc[i]) < len(d) / 2:
                while d[0] != loc[i]:
                    d.append(d.popleft())
                    ans += 1
            else:
                while d[0] != loc[i]:
                    d.appendleft(d.pop())
                    ans += 1
print(ans)
