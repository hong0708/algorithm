# https://www.acmicpc.net/problem/20529

import sys
from itertools import combinations

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    arr = list(sys.stdin.readline().rstrip().split())
    ans = 12
    if n > 32:
        print(0)
    else:
        for i in combinations(arr, 3):
            i = list(i)
            res = 0
            for a in range(3):
                for b in range(a + 1, 3):
                    for c in range(4):
                        if i[a][c] != i[b][c]:
                            res += 1
            ans = min(ans, res)
        print(ans)
