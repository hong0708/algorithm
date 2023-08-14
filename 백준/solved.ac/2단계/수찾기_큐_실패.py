# https://www.acmicpc.net/problem/1920

from collections import deque

n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr3 = list(map(int, input().split()))
arr1.sort()
arr2 = list(set(sorted(arr3)))
ans = []

test = {}

for i in arr3:
    test[i] = 0

impl = deque(arr1)
loc = 0

while impl and loc < len(arr2):
    num = impl.popleft()
    if num == arr2[loc]:
        #while loc < len(arr2) and num == arr2[loc]:
        ans.append([arr2[loc], 1])
        loc += 1
    else:
        while loc < len(arr2) and num > arr2[loc]:
            ans.append([arr2[loc], 0])
            loc += 1
if len(arr2) - 1 > loc:
    for i in range(loc, len(arr2)):
        ans.append([arr2[i], 0])

for i in range(len(ans)):
    test[ans[i][0]] = ans[i][1]

for i in arr3:
    print(test[i])