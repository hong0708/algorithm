# https://www.acmicpc.net/problem/15663

n, m = map(int, input().split())
arr = list(map(int, input().split()))
visited = [0 for _ in range(n)]
arr.sort()


def b(a):
    if len(a) == m:
        print(*a)
    else:
        impl = []
        for i in range(n):
            if not visited[i] and arr[i] not in impl:
                a.append(arr[i])
                impl.append(arr[i])
                visited[i] = 1
                b(a)
                visited[i] = 0
                a.pop()


b([])
