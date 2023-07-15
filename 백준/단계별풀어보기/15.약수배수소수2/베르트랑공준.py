while True:
    n = int(input())
    if n == 0:
        break
    else:
        answer = 0
        arr = [True, True] + [False for _ in range(2 * n)]
        for i in range(2, int(len(arr) ** 0.5) + 1):
            if not arr[i]:
                for j in range(2 * i, len(arr), i):
                    arr[j] = True

        for a in range(n + 1, 2 * n + 1):
            if not arr[a]:
                answer += 1
        print(answer)
