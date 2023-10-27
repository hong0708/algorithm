# https://www.acmicpc.net/problem/11052

# n개의 카드 구매를 위한 n 종류의 카트팩 종류는 개수를 표현한다
n = int(input())
p = [0] + list(map(int, input().split()))
dp = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i - j] + p[j])
print(dp[n])
