# https://www.acmicpc.net/problem/8958

n = int(input())
for _ in range(n):
    arr = input()

    ans = 0
    count = 0

    for i in arr:
        if i == 'O':
            count += 1
            ans += count
        elif i != 'O':
            count = 0

    print(ans)
