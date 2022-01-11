# https://www.acmicpc.net/problem/18870
import sys

r = sys.stdin.readline

n = int(r())
num_list = list((map(int, input().split())))

count = sorted(list(set(num_list)))

dic = {count[i] : i for i in range(len(count))}
for i in num_list:
    print(dic[i], end = ' ')