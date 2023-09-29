# https://www.acmicpc.net/problem/2212

import sys

n = int(input())
k = int(input())
road = list(map(int, sys.stdin.readline().split()))
road.sort()

arr = []
for i in range(1, n):
    arr.append(road[i] - road[i - 1])
arr.sort()

print(sum(arr[:n - k]))
