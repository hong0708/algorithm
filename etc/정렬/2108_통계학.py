import sys

from collections import Counter

r = sys.stdin.readline

n = int(r())
num_list = []

for _ in range(n):
    num = int(r())
    num_list.append(num)

num_list.sort()

mode = Counter(num_list).most_common(2)
# (2) -> 가장 많이 나온 두개까지
print(round(sum(num_list) / len(num_list)))
print(num_list[len(num_list) // 2])
#print(mode[1][0] if len(mode) > 1 and mode[0][1] == mode[1][1] else mode[0][0])
if len(mode) > 1:  # 만약 입력값이 하나면 , 그게 최빈값이 되므로 예외처리
    if mode[0][1] == mode[1][1]:
        print(mode[1][0])
    # 최빈값의 빈도수를 비교하여, 2개이상의 최빈값이 있으면 두번째로 작은것을 출력
    else:
        print(mode[0][0])
else:
    print(mode[0][0])
print(num_list[-1] - num_list[0])
