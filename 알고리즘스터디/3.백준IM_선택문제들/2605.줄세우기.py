n = int(input())
data = list(map(int, input().split()))
answer = []

count = 1
for i in range(n):
    if data[i] == 0:
        answer = [count] + answer
    elif data[i] == count - 1:
        answer.append(count)
    else:
        answer = answer[:data[i]] + [count] + answer[data[i]:]
    count += 1
answer.reverse()
for j in answer:
    print(j, end=' ')
