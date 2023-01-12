#https://www.acmicpc.net/problem/2750

n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))
#array.sort()
array = sorted(array)

for i in array:
    print(i)