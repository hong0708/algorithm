# https://www.acmicpc.net/problem/11050

n, k = map(int, input().split())
arr = [1 for _ in range(11)]


def f(a):
    ans = 0
    if a == 1:
        return 1
    else:
        ans = a * f(a - 1)
        arr[a] = ans
        return ans


f(n)
print(arr[n] // (arr[k] * arr[n - k]))
