# https://www.acmicpc.net/problem/18870
import sys

r = sys.stdin.readline

n = int(r())
num_list = list((map(int, input().split())))

count = []
for _ in range(n):
    count.append(0)

for i in range(len(num_list)):
    for j in range(len(num_list)):
        if num_list[i] > num_list[j]:
            count[i] += 1
for i in count:
    print(i, end=' ')
#시간 초과, 값은 나오는데 범위 생각못함 바보임 