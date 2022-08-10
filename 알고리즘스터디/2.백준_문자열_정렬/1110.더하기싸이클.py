orgNum = int(input())
num = orgNum
count = 0
while 1:
    count += 1
    rightNum = (num % 10)
    leftNum = rightNum + num // 10
    leftNum %= 10
    num = rightNum * 10 + leftNum
    if num == orgNum:
        break
print(count)