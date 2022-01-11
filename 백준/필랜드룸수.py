while True:
    num = list(input())
    if num[0] == '0':
        break
    pos = 0
    if len(num) == 1:
        print('yes')
    else:
        while pos < len(num) // 2:
            if num[pos] != num[-(pos + 1)]:
                print('no')
                break
            pos += 1
            if pos == len(num) // 2:
                print('yes')
                break
