tc = int(input())
for t in range(tc):

    arr = list(map(int, input().split()))

    arr.sort()
    minNum = min(arr)
    maxNum = max(arr)
    arr.remove(minNum)
    arr.remove(maxNum)

    avg = sum(arr) / 8

    print("#{} {}".format(t + 1, ))