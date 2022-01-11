from _collections import deque

n = int(input())
nums = list(map(int, input().split()))

stack = deque()
right_big = [-1] * n
for i in range(n):
    while stack:
        if stack[-1][0] < nums[i]:
            last, where = stack.pop()
            right_big[where] = nums[i]
        else:
            break
    stack.append([nums[i], i])
print(right_big)


from _collections import deque

n = int(input())
nums = list(map(int, input().split()))

stack = deque()
right_big = [-1] * n
for i in range(n):
    while stack and stack[-1][0] < nums[i]:
        last, where = stack.pop()
        right_big[where] = nums[i]
    stack.append([nums[i], i])
print(*right_big)
