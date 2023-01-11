NUM = 1000000007


def find(m, n, data):
    if m == 0 and n == 0:
        return 1
    elif data[n][m] == -1:
        return 0

    elif data[n][m] != -1:
        if data[n][m] > 0:
            return data[n][m]
        else:
            if m - 1 > -1 and n - 1 > -1:
                data[n][m] = (find(m, n - 1, data) + find(m - 1, n, data)) % NUM
            elif m - 1 > -1:
                data[n][m] = (find(m - 1, n, data)) % NUM
            elif n - 1 > -1:
                data[n][m] = (find(m, n - 1, data)) % NUM
    return data[n][m]


def solution(m, n, puddles):
    data = [[0 for _ in range(m)] for _ in range(n)]
    for i in puddles:
        data[i[1] - 1][i[0] - 1] = -1
    data[0][0] = 1
    answer = find(m - 1, n - 1, data)
    return answer
