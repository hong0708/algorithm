# https://www.acmicpc.net/problem/1764

n, m = map(int, input().split())

arr1 = []
arr2 = []
for i in range(n):
    x = input()
    arr1.append(x)

for i in range(m):
    y = input()
    arr2.append(y)

arr1 = set(arr1)
arr2 = set(arr2)

answer = list(arr1 & arr2)
answer.sort()
print(len(answer))
for a in answer:
    print(a)
