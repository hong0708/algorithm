t = int(input())
for tc in range(1, t + 1):
    k = int(input())
    w = input()
    w_list = []

    for i in range(len(w)):
        for j in range(1, len(w) + 1):
            w_list.append(w[i:i + j])

    w_list = list(set(w_list))
    w_list.sort()
    if k < len(w_list):
        answer = w_list[k - 1]
    else:
        answer = 'none'

    print("#{} {}".format(tc, "".join(answer)))
