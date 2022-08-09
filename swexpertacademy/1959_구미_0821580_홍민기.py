tc = int(input())
for t in range(tc):
    max = 0
    a, b = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    if a > b:
        gap = a - b
        for i in range(0, gap + 1):
            count = 0
            for j in range(0, b):
                count += arr1[j + i] * arr2[j]
            if max < count:
                max = count
    else:
        gap = b - a
        for i in range(0, gap + 1):
            count = 0
            for j in range(0, a):
                count += arr2[j + i] * arr1[j]
            if max < count:
                max = count
    answer = max
    print("#{} {}".format(t + 1, answer))
