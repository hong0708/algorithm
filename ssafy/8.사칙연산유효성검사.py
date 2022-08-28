for t in range(10):
    N = int(input())
    answer = 1
    for n in range(N):
        data = list(input().split())
        if not data[1].isdigit():
            if len(data) < 4:
                answer = 0
    print("#{} {}".format(t + 1, answer))
