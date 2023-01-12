# https://www.acmicpc.net/problem/10814
import sys

r = sys.stdin.readline
num_list = []
n = int(r())
for i in range(n):
    num_list.append(list(input().split()))

num_list.sort(key=lambda x: int(x[0]))
for i, j in num_list:
    print(i, j)
