# https://www.acmicpc.net/problem/2164
from collections import deque

n = int(input())

arr = deque()
for i in range(1, n + 1):
    arr.append(i)
loc = 0
while len(arr) > 1:
    if loc % 2 == 1:
        num = arr.popleft()
        arr.append(num)
    else:
        arr.popleft()
    loc += 1
print(arr[0])
