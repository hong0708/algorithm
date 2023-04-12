import math


def solution(n, k):
    answer = []
    impl = [i for i in range(1, n + 1)]

    while n > 0:
        a = k // math.factorial(n - 1)
        if k % math.factorial(n - 1) == 0:
            answer.append(impl[a - 1])
            impl.pop(a - 1)
        else:
            answer.append(impl[a])
            impl.pop(a)
        k %= math.factorial(n - 1)
        n -= 1
    return answer
