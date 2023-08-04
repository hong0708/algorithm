# https://www.acmicpc.net/problem/11659
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

p = [0]

for a in range(len(arr)):
    p.append(p[a] + arr[a])

for _ in range(m):
    i, j = map(int, input().split())
    print(p[j] - p[i - 1])
