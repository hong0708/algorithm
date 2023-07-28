# https://www.acmicpc.net/problem/9251

a = input()
b = input()
la = len(a)
lb = len(b)

arr = [0 for _ in range(lb)]

for i in range(la):
    v = 0
    for j in range(lb):
        if v < arr[j]:
            v = arr[j]
        elif a[i] == b[j]:
            arr[j] = v + 1
print(max(arr))
