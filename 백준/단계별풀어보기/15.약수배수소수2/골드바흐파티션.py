t = int(input())
arr = [True, True] + [False for _ in range(1000000)]
p = []

for i in range(2, int(len(arr) ** 0.5) + 1):
    if not arr[i]:
        p.append(i)
        for j in range(2 * i, len(arr), i):
            arr[j] = True

for _ in range(t):
    n = int(input())
    impl = []
    answer = 0
    for a in p:
        if n < a:
            break
        if not arr[n - a]:
            if a <= n - a:  # 중복된 케이스를 제거하기 위해 절반만 확인
                answer += 1
    print(answer)
