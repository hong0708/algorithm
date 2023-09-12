# https://www.acmicpc.net/problem/17219

import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
dic = {}
for _ in range(n):
    s, p = input().rstrip().split()
    dic[s] = p
for _ in range(m):
    a = input().rstrip()
    print(dic[a])
