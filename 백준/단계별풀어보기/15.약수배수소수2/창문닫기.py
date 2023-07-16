n = int(input())
answer = 1
if n < 4:
    print(answer)
else:
    for i in range(2, n):
        if i ** 2 <= n:
            answer += 1
        else:
            break
    print(answer)
