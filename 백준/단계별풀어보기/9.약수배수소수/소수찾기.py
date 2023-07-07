n = int(input())
answer = 0
arr = [False, False] + [True for _ in range(1000)]
impl = list(map(int, input().split()))
maxNum = max(impl)
for i in range(2, maxNum):
    for j in range(2 * i, maxNum + 1, i):
        arr[j] = False

for a in impl:
    if arr[a]: answer += 1
print(answer)
