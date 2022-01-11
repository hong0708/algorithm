how = 0
total = 0
for i in range(5):
    a = list(map(int, input().split()))
    point = 0
    for j in a:
        point += j
    if total < point:
        total = point
        how = i + 1
print((how) + ' ' + (total))
