# https://www.acmicpc.net/problem/10951
# 입력 예외 상황

while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break