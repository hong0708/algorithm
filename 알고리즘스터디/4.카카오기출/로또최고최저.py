def solution(lottos, win_nums):
    rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    count_ok = 0
    count_zero = 0

    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            count_ok += 1
        if lottos[i] == 0:
            count_zero += 1

    total = count_ok + count_zero

    answer = [rank[total], rank[count_ok]]
    return answer