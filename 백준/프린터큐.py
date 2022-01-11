N = int(input())
while N:
    count_where = list(map(int, input().split()))
    numlist = list(map(int, input().split()))

    where = count_where[1]
    count = 0

    fin = True
    while fin:
        if where == 0:
            if numlist[0] == max(numlist):
                numlist = numlist[1:]
                count += 1
                break
            else:
                back = numlist[0]
                numlist = numlist[1:]
                numlist.append(back)
                where = len(numlist) - 1
        else:
            if numlist[0] == max(numlist):
                numlist = numlist[1:]
                count += 1
                break
            else:
                back = numlist[0]
                numlist = numlist[1:]
                numlist.append(back)
                where = len(numlist) - 1
    N -= 1
    print (count)
