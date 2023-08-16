# https://www.acmicpc.net/problem/4153

while True:
    arr = list(map(int, input().split()))
    arr.sort()
    if sum(arr) == 0:
        break
    else:
        if arr[1] ** 2 + arr[0] ** 2 == arr[2] ** 2:
            print('right')
        else:
            print('wrong')
