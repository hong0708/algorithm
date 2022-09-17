def multiNum(number, i):
    if i == 1:
        return number
    return multiNum(number, i - 1) * number


for t in range(10):
    tc = int(input())
    num, multi = map(int, input().split())
    answer = multiNum(num, multi)

    print("#{} {}".format(t + 1, answer))
