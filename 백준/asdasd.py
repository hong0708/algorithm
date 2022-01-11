n, k = map(int, input().split())
local = [0] * 100001


def find(n):
    while 0 == local[k]:
        where = n
        time = local[n] + 1

        if 0 <= where + 1 < 100001 and not local[where + 1]:
            local[where + 1] = time + 1
            find(where + 1)
        if 0 <= where - 1 < 100001 and not local[where - 1]:
            local[where - 1] = time + 1
            find(where - 1)
        if 0 <= where * 2 < 100001 and not local[where * 2]:
            local[where * 2] = time + 1
            find(where * 2)
    print (local[k])


find(n)

import sys
from collections import deque

input = sys.stdin.readline()


def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(local[x])
            break
        for j in (x - 1, x + 1, x * 2):
            if 0 <= j <= MAX and not local[j]:
                if j == x * 2:
                    q.append(j)
                else:
                    local[j] = local[x] + 1
                    q.append(j)
MAX = 100000
n, k = map(int, input.split())
local = [0] * (MAX + 1)
bfs()
