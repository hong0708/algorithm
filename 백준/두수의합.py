#https://www.acmicpc.net/problem/3273
#투포인터
n = int(input())
numList = list(map(int, input().split()))
x = int(input())

numList.sort()

answer = 0
left, right = 0, n-1 # 왼쪽, 오른쪽
while left < right:
    temp = numList[left] + numList[right]
    if temp == x:
        answer += 1
        left += 1
    elif temp < x:
        left += 1
    else:
        right -= 1
print(answer)