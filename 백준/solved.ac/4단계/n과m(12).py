# https://www.acmicpc.net/problem/15666

n, m = map(int, input().split())
arr = list(map(int, input().split()))

ans = []


def make(a):
    if not len(a):
        impl = []
        for i in arr:
            if i not in impl:
                make(a + [i])
                impl.append(i)
    elif len(a) == m:
        ans.append(a)
    else:
        impl = []
        for i in arr:
            if a[-1] <= i and i not in impl:
                make(a + [i])
                impl.append(i)


make([])
ans.sort()
for i in ans:
    print(*i)