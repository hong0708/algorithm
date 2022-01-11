# https://www.acmicpc.net/problem/15649
n, m = map(int, input().split())

num_list = []
check = [True] * n

def back(depth, N, M):
    if depth == M:
        for i in num_list:
            print(i, end=' ')
        print()
        return
    for j in range(1, n + 1):
        if check[j-1]:
            check[j-1] = False
            num_list.append(j)
            back(depth + 1, N, M)
            check[j-1] = True
            num_list.pop()


back(0, n, m)
