N, K = map(int, input().split())
lst = []
for i in range(1, N + 1):
    if N % i == 0:
        lst.append(i)

if len(lst) < K:  # 약수의 개수가 K보다 작을 때
    print(0)
else:
    print(lst[K - 1])  # 인덱스 번호에 맞춰서 K-1번째로 해야함
