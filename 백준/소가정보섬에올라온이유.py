n, q = map(int, input().split())
cow = list(map(int, input().split()))
makeMiss = list(map(int, input().split()))

# 미리 곱
subAdd = [0] * n
for i in range(n):
    subAdd[i] = cow[i] * cow[i - 1] * cow[i - 2] * cow[i - 3]

ex_sum = sum(subAdd)
for idx in makeMiss:
    for i in range(4):
        new_idx = (idx - 1 + i) % n
        subAdd[new_idx] = -subAdd[new_idx]
        ex_sum += 2 * subAdd[new_idx]
    print(ex_sum)
