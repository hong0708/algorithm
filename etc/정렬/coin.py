n, k = map(int, input().split())

# 코인의 종류
c = [int(input()) for i in range(n)]
# 사이즈 k+1 만큼의 리스트 선언
dp = [0 for i in range(k + 1)]
# 인덱스 0은 동전 1개만을 사용할 때의 경우 대비
dp[0] = 1

for i in c:
    for j in range(i, k + 1):
        if j - i >= 0:
            dp[j] += dp[j - i]
print (dp[k])
