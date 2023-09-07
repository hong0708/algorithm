# https://www.acmicpc.net/problem/5525

n = int(input())
m = int(input())
arr = input()

ans = [0 for _ in range(m)]

loc = 0
while loc < m:
    if arr[loc] == "I":
        count = 0
        start = loc
        next = True
        while loc < m:
            # I 가 올 차례 인데 I 옴
            if next and arr[loc] == "I":
                loc += 1
                next = False
                if loc == m:
                    ans[start] = count
            # O 가 올 차례 인데 O 옴
            elif not next and arr[loc] == "O":
                loc += 1
                count += 1
                next = True
                if loc == m:
                    ans[start] = count - 1
            # I가 올 차례 인데 O가 옴
            elif next and arr[loc] == "O":
                ans[start] = count - 1
                break
            # O가 올 차례 인데 I가 옴
            elif not next and arr[loc] == "I":
                ans[start] = count
                break
    else:
        loc += 1

answer = 0
for i in ans:
    if i - n + 1 > 0:
        answer += (i - n + 1)
print(answer)
