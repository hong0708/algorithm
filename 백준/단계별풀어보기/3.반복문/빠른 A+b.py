# https://www.acmicpc.net/problem/15552
# readline 속도에 관한 내용
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)
