#https://www.acmicpc.net/problem/11650

N = int(input())
nums = []
for i in range(N):
    [a, b] = map(int, input().split())
    nums.append([a, b])
nums = sorted(nums)
#num.sort(key=lambda x:(x[0],x[1]))
for i in range(N):
    print(nums[i][0], nums[i][1])

