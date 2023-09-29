# https://www.acmicpc.net/problem/9252

a = input()
b = input()
la = len(a)
lb = len(b)
ans = [[['', 0] for _ in range(lb + 1)] for _ in range(la + 1)]
for i in range(1, la + 1):
    for j in range(1, lb + 1):

        if a[i - 1] == b[j - 1]:
            ans[i][j][1] = ans[i - 1][j - 1][1] + 1
            ans[i][j][0] = ans[i - 1][j - 1][0] + a[i - 1]
        else:
            if ans[i][j - 1][1] > ans[i - 1][j][1]:
                ans[i][j][1] = ans[i][j - 1][1]
                ans[i][j][0] = ans[i][j - 1][0]
            else:
                ans[i][j][1] = ans[i - 1][j][1]
                ans[i][j][0] = ans[i - 1][j][0]

print(ans[la][lb][1])
print(ans[la][lb][0])