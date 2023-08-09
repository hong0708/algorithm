# https://www.acmicpc.net/problem/17299

from collections import deque
from collections import Counter

n = int(input())
# 각 위치에 있는 숫자
arr = list(map(int, input().split()))

ans = [-1 for _ in range(n)]
l = Counter(arr)
d = deque()

# 각 위치에 따라 저장하며 넘어감
for i in range(n):
    # 만약 현재 위치의 개수가 저장된 마지막 위치 숫자보다 많다면 해당 위치의 정답을 갱신
    while d and d[-1][1] < l[arr[i]]:
        c = d.pop()
        ans[c[0]] = arr[i]
    d.append([i, l[arr[i]]])

print(*ans)
