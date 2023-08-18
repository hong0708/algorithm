# https://www.acmicpc.net/problem/9663

n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]
ans = 0
visited = [-1 for _ in range(n)]


def queen(c):
    global ans
    if c == n:
        ans += 1
        return

    for j in range(0, n):
        if check(c, j):
            arr[c][j] = 1
            visited[c] = j

            queen(c + 1)

            arr[c][j] = 0
            visited[c] = -1


def check(x, y):
    for i in range(0, x):
        if y == visited[i] or x - i == y - visited[i] or x - i == visited[i] - y:
            return False
    return True


queen(0)
print(ans)
