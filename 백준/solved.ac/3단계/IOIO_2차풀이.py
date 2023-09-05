# https://www.acmicpc.net/problem/5525

n = int(input())
m = int(input())
arr = input()

loc, count, ans = 0, 0, 0

while loc < m - 1:
    if arr[loc:loc + 3] == 'IOI':
        loc += 2
        count += 1
        if count == n:
            ans += 1
            count -= 1
    else:
        loc += 1
        count = 0
print(ans)
