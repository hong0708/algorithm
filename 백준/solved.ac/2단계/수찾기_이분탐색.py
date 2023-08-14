# https://www.acmicpc.net/problem/1920

n = int(input())
arr1 = list(map(int, input().split()))
arr1.sort()

m = int(input())
arr2 = list(map(int, input().split()))

for i in arr2:
    start = 0
    end = n - 1
    while True:
        m = (start + end) // 2
        if i == arr1[m]:
            print(1)
            break
        elif i > arr1[m]:
            start = m + 1

        elif i < arr1[m]:
            end = m - 1

        if start > end:
            print(0)
            break
