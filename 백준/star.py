star = ['*']
blank = [' ']

line = int(input())

for i in range(line):
    if i == line - 1:
        print(star[0] * ((i + 1) * 2 - 1))

    elif i == 0:
        print(blank[0] * (line - 1) + star[0])

    else:
        print(blank[0] * (line - i - 1) + star[0] + blank[0] * (i * 2 - 1) + star[0])

