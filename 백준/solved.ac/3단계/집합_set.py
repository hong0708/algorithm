# https://www.acmicpc.net/problem/11723

import sys

m = int(input())
arr = set()
for _ in range(m):
    impl = sys.stdin.readline().strip().split()

    if len(impl) == 1:
        if impl[0] == 'all':
            x = 'arr'
            arr = set([i for i in range(1, 21)])
        elif impl[0] == 'empty':
            arr = set()
    else:
        x, y = impl[0], impl[1]
        y = int(y)
        if x == 'add':
            arr.add(y)
        elif x == 'remove':
            arr.discard(y)
        elif x == 'check':
            print(1 if y in arr else 0)
        elif x == 'toggle':
            if y in arr:
                arr.discard(y)
            else:
                arr.add(y)
