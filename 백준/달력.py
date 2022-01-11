day = [0] * 366
n = int(input())
count = 0
start = 0
for _ in range(n):
    start, end = map(int, input().split())
    for i in range(start, end + 1):
        day[i] += 1

max = 0
i = 0
while True:
    if i == 365:
        break
    elif day[i] > 0:
        for j in range(i, 366):
            if day[j] > max:
                max = day[j]
            elif j == 365:
                count += max * (j - i)
                i = j
                break
            elif day[j] == 0:
                count += max * (j - i)
                i = j
                break
    else:
        i += 1
        max = 0
print(count)