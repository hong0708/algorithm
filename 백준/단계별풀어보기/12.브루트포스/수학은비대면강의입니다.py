arr = list(map(int, input().split()))
for i in range(-999, 1000):
    for j in range(-999, 1000):
        if arr[0] * i + arr[1] * j == arr[2] and arr[3] * i + arr[4] * j == arr[5]:
            print(i, j)
