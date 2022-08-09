tc = int(input())
for t in range(tc):
    str = input()
    grass = list(str)
    count = 0
    for i in range(len(grass)):
        if grass[i] == '(':
            count += 1
        elif grass[i] == ')':
            if grass[i-1] == '|':
                count += 1

    print("#{} {}".format(t + 1, count))
