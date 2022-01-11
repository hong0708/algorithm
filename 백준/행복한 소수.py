n = 10000
a = [False, False] + [True] * (n - 1)
primes = []

for i in range(2, n + 1):
    if a[i]:
        primes.append(i)
        for j in range(2 * i, n + 1, i):
            a[j] = False

def happy(case, num):
    list = [num]
    while True:
        num = list[-1]
        one = []
        next_num = 0
        while True:
            if num // 10 == 0:
                one.append(num)
                break
            one.append(num % 10)
            num = num // 10
        for i in one:
            next_num += (i * i)
        list.append(next_num)
        if list.count(next_num) == 2:
            print(str(case) + ' ' + str(list[0]) + ' ' + 'NO')
            break
        if next_num == 1:
            print(str(case) + ' ' + str(list[0]) + ' ' + 'YES')
            break


p = int(input())
for _ in range(p):
    case, num = map(int, input().split())
    if num in primes:
        happy(case, num)
    else:
        print(str(case) + ' ' + str(num) + ' ' + 'NO')
