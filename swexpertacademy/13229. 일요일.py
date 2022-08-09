days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
tc = int(input())
for t in range(tc):
    day = input()

    if day == days[0]:
        answer = 6
    elif day == days[1]:
        answer = 5
    elif day == days[2]:
        answer = 4
    elif day == days[3]:
        answer = 3
    elif day == days[4]:
        answer = 2
    elif day == days[5]:
        answer = 1
    elif day == days[6]:
        answer = 7

    print("#{} {}".format(t + 1, answer))
