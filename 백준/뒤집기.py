arr = input()
answer = 1000000
for a in range(2):
    count = 0
    fix = a % 2
    change = False

    for i in range(len(arr)):
        if change == False and fix != int(arr[i]):
            count += 1
            change = True
        if change == True and fix == int(arr[i]):
            change = False
    answer = min(answer, count)
print(answer)
