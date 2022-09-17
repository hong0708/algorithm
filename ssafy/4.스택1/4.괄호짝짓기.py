for t in range(10):
    tc = int(input())
    data = list(map(str, input()))
    count = [0, 0, 0]

    answer = 1
    if data.count('{') != data.count('}'):
        answer = 0
    elif data.count('[') != data.count(']'):
        answer = 0
    elif data.count('(') != data.count(')'):
        answer = 0

    print("#{} {}".format(t + 1, answer))
