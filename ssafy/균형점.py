def search(start, end):
    mid = 0
    while (end - start) >= 1 / (10 ** 12):
        mid = (start + end) / 2
        left, right = 0, 0
        for a in range(numX):
            force = weight[a] / (mid - x[a]) ** 2

            if x[a] < mid:
                left += force
            else:
                right += force

        if left > right:
            start = mid
        else:
            end = mid
    return mid

t = int(input())
for tc in range(1, t+1):
    numX = int(input())
    arr = list(map(int, input().split()))
    answer = []
    x = arr[:numX]
    weight = arr[numX:]


    for i in range(0, numX - 1):
        answer.append(search(x[i], x[i + 1]))
    print("#{} {}".format(tc,' '.join('%.10f' % f for f in answer)))