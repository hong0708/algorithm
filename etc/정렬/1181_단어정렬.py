# https://www.acmicpc.net/problem/1181
num_list = []
n = int(input())

for i in range(n):
    num_list.append(input())
set_num_list = list(set(num_list))

set_num_list.sort(key=lambda x: (len(x), x))

for j in set_num_list:
    print(j)
    
# 람다 사용까지 잘했는데  , x  추가 조건 때문에 좀 걸림