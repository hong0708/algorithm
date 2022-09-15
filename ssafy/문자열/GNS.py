t = int(input())
for tc in range(1, t + 1):
    skip = input()
    d_nums = {"ZRO": 0, "ONE": 0, "TWO": 0, "THR": 0, "FOR": 0, "FIV": 0, "SIX": 0, "SVN": 0, "EGT": 0, "NIN": 0}
    data = list(map(str, input().split()))

    for i in range(len(data)):
        d_nums[data[i]] += 1

    answer = ''
    for a, b in d_nums.items():
        temp = ' '.join([a] * b)
        answer += temp + ' '

    print("#{} {}".format(tc, answer[:len(answer) - 1]))
