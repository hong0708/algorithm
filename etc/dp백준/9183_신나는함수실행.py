# https://www.acmicpc.net/problem/9184
# 함수 자체를 바꾸자 했으나 그냥 범위를 줄이고 이미 나온 값을 저장해두는 식도 있다
answer = {}

def fun(a, b, c):
    if (a, b, c) in answer:
        return answer[(a, b, c)]
    else:
        if a <= 0 or b <= 0 or c <= 0:
            answer[(a, b, c)] = 1
            return 1

        if a > 20 or b > 20 or c > 20:
            answer[(a, b, c)] = fun(a, b, c)
            return fun(20, 20, 20)

        if a < b < c:
            answer[(a, b, c)] = fun(a, b, c - 1) + fun(a, b - 1, c - 1) - fun(a, b - 1, c)
            return fun(a, b, c - 1) + fun(a, b - 1, c - 1) - fun(a, b - 1, c)

        answer[(a, b, c)] = fun(a - 1, b, c) + fun(a - 1, b - 1, c) + fun(a - 1, b, c - 1) - fun(a - 1, b - 1, c - 1)
        return fun(a - 1, b, c) + fun(a - 1, b - 1, c) + fun(a - 1, b, c - 1) - fun(a - 1, b - 1, c - 1)


while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print('w(' + str(a) + ',' + str(b) + ',' + str(c) + ') = ' + str(fun(a, b, c)))
