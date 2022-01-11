N = int(input())

answer = 0

timeList = list(map(int, (input().split())))

timeList.sort()
print(timeList)

for i in range(N):
    answer += timeList[i] * (N - i)
print(answer)
