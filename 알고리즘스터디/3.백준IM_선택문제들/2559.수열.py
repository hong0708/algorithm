# 2~k+1번째 수의 합은 1~k번째 수의 합에서 1번째 수를 빼고, k+1번째 수를 더한 값과 같다.
n, day = map(int, input().split())
data = list(map(int, input().split()))

maxTemp = sum(data[0:day])
beforeNum = sum(data[0:day])

if day == 1:
    print(max(data))
else:

    for i in range(1, n - day + 1):
        if maxTemp < beforeNum - data[i - 1] + data[i + day - 1]:
            maxTemp = beforeNum - data[i - 1] + data[i + day - 1]
        beforeNum = beforeNum - data[i - 1] + data[i + day - 1]
    print(maxTemp)
