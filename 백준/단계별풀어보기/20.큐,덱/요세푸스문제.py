# https://www.acmicpc.net/problem/11866
def location(num, add, divide):
    num += add
    return num % divide


n, k = map(int, input().split())
arr = []
visited = [False for _ in range(n)]
visited[k - 1] = True
ans = [k]

for i in range(1, n + 1):
    arr.append(i)
count = 1
loc = k - 1

while count < n:
    turn = 0
    while turn <= k:
        if not visited[loc]:
            turn += 1
            if turn == k:
                visited[loc] = True
                ans.append(arr[loc])
                break
        loc = location(loc, 1, n)
    count += 1

print('<', end='')
for i in range(n):
    if i != n - 1:
        print(f'{ans[i]}, ', end="")
    else:
        print(f'{ans[i]}', end="")
print('>', end="")
