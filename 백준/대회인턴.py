n, m, k = map(int, input().split())
answer = 0
if n > m * 2:
    answer = m
    if k > n - (m * 2):
        if k - (n - (m * 2)) % 3 != 0:
            answer -= k - (n - (m * 2)) // 3
            answer -= 1
        else:
            answer -= k - (n - (m * 2)) // 3
elif n < m * 2:
    answer = n // 2
    if n % 2 != 0:
        k -= 1
    if k > m - (n // 2):
        if k - (m - (n // 2)) % 3 != 0:
            answer -= k - (m - (n // 2)) // 3
            answer -= 1
        else:
            answer -= k - (m - (n // 2)) // 3
else:
    answer = m
    if k % 3 != 0:
        answer -= k // 3
        answer -= 1
    else:
        answer -= k // 3
print(answer)