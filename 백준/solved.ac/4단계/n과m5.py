# https://www.acmicpc.net/problem/15654

n, m = map(int, input().split())
arr = list(map(int, input().split()))
visited = [1 for _ in range(n)]
ans = []
arr.sort()


def b(a):
    if len(a) == m:
        print(*a)
    else:
        for i in range(n):
            if visited[i]:
                a.append(arr[i])
                visited[i] = 0
                b(a)
                a.pop()
                visited[i] = 1


b(ans)
