# https://www.acmicpc.net/problem/1208

from itertools import combinations

n, s = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

arr1 = arr[:n // 2]
arr2 = arr[n // 2:]
arr1_sum = []
arr2_sum = []

for i in range(len(arr1) + 1):
    for j in combinations(arr1, i):
        arr1_sum.append(sum(j))
arr1_sum.sort()

for i in range(len(arr2) + 1):
    for j in combinations(arr2, i):
        arr2_sum.append(sum(j))
arr2_sum.sort(reverse=True)

r, l = 0, 0
while l < len(arr1_sum) and r < len(arr2_sum):
    ls, rs = arr1_sum[l], arr2_sum[r]
    ad = ls + rs
    if ad == s:
        # 중복된 경우를 찾아야함
        impl_l, impl_r = l, r
        while impl_l < len(arr1_sum) and arr1_sum[impl_l] == ls:
            impl_l += 1
        while impl_r < len(arr2_sum) and arr2_sum[impl_r] == rs:
            impl_r += 1
        ans += (impl_l - l) * (impl_r - r)
        l, r = impl_l, impl_r

    elif ad > s:
        r += 1
    else:
        l += 1

if s == 0:
    print(ans - 1)
else:
    print(ans)
