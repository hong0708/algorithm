t = int(input())

for _ in range(t):
    n = int(input())
    arr = [0, 1, 2, 4, 7] + [0 for _ in range(7)]
    for i in range(n + 1):
        if -1 < i < 5:
            if i == n:
                print(arr[i])
                break
        else:
            arr.append(arr[i - 1] + arr[i - 2] + arr[i - 3])
            if i == n:
                print(arr[i])
                break
