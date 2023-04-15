t = []


def calculation(be, af, b_time, b_fee, m, f):
    count = 0
    time = (int(af[:2]) - int(be[:2])) * 60 + int(af[3:]) - int(be[3:])
    if time - b_time > 0:
        if (time - b_time) % m == 0:
            count += (time - b_time) // m * f + b_fee
        else:
            count += (time - b_time) // m * f + b_fee + f
    else:
        count = b_fee
    return count


def add(car, time):
    if t:
        for i in range(len(t)):
            if t[i][0] == car:
                t[i][1] += time
                return
        t.append([car, time])
    else:
        t.append([car, time])


def solution(fees, records):
    answer = []
    cars = []

    for i in records:
        if i[-1] == 'N':
            cars.append(i)
        else:
            for j in range(len(cars)):
                if cars[j][6:10] == i[6:10]:
                    time = (int(i[:2]) - int(cars[j][:2])) * 60 + int(i[3:5]) - int(cars[j][3:5])
                    add(cars[j][6:10], time)
                    cars.pop(j)
                    break
    if cars:
        for z in cars:
            time = (23 - int(z[:2])) * 60 + 59 - int(z[3:5])
            add(z[6:10], time)

    t.sort(key=lambda x: x[0])

    for i in range(len(t)):
        if t[i][1] > fees[0]:
            if (t[i][1] - fees[0]) % fees[2] == 0:
                answer.append(fees[1] + ((t[i][1] - fees[0]) // fees[2]) * fees[3])
            else:
                answer.append(fees[1] + ((t[i][1] - fees[0]) // fees[2] + 1) * fees[3])
        else:
            answer.append(fees[1])

    return answer
