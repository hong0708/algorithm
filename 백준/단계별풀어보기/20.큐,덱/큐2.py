# https://www.acmicpc.net/problem/18258
from collections import deque
import sys

n = int(input())
arr = deque()

for _ in range(n):
    com = sys.stdin.readline().rstrip()
    if com[:4] == "push":
        arr.append(com[5:])

    elif com == "pop":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.popleft())
    elif com == "size":
        print(len(arr))
    elif com == "empty":
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif com == "front":
        if len(arr) > 0:
            print(arr[0])
        else:
            print(-1)
    else:
        if len(arr) > 0:
            print(arr[-1])
        else:
            print(-1)
