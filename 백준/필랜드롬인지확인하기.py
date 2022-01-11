
num = list(input())
pos = 0
if len(num) == 1:
    print('yes')
while pos < len(num) // 2:
    if num[pos] != num[-(pos + 1)]:
        print('0')
        break
    pos += 1
    if pos == len(num) // 2:
        print('1')
        break