N = int(input())
Time, Pay = [], []
for _ in range(N):
    t, p = map(int, input().split())
    Time.append(t)
    Pay.append(p)

money = [0] * (N + 1)

for i in range(N - 1, -1, -1):
    # i일에 상담을 하는 것이 퇴사일을 넘기면 상담 ㄴㄴ
    if i + Time[i] > N:
        money[i] = money[i + 1]
    else:
        # i일에 상담을 하는 것과 상담을 안하는 것 중 큰 것을 선택
        money[i] = max(money[i + 1], Pay[i] + money[i + Time[i]])

print(money[0])