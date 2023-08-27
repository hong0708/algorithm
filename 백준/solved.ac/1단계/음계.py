# https://www.acmicpc.net/problem/2920

arr = [1, 2, 3, 4, 5, 6, 7, 8]
reverse = sorted(arr, reverse=True)

impl = list(map(int, input().split()))
asc = True
des = True

for i in range(8):
    if arr[i] != impl[i]:
        asc = False
    if reverse[i] != impl[i]:
        des = False

if asc:
    print('ascending')
elif des:
    print('descending')
else:
    print('mixed')
