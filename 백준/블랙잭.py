from itertools import combinations
n, m = map(int, input().split())
arr = list(map(int, input().split()))
max = 0
for num in combinations(arr, 3):
    black_sum = sum(num)
    if max < black_sum <= m:
        max = black_sum
print (max)
