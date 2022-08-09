tc = int(input())
for t in range(tc):
    str = input()
    arms = list(str)

    trycount = 15 - len(arms)
    win = 8 - arms.count('o')
    if trycount < win:
        print("#{} {}".format(t + 1, 'NO'))
    else:
        print("#{} {}".format(t + 1, 'YES'))
