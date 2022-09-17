for t in range(10):
    tc = int(input())
    target = list(map(str, input()))
    data = list(map(str, input()))
    answer = 0

    for i in range(len(data) - len(target) + 1):
        for j in range(len(target)):
            if data[i + j] != target[j]:
                break
            else:
                if j == len(target) - 1:
                    answer += 1
    print("#{} {}".format(t + 1, answer))
