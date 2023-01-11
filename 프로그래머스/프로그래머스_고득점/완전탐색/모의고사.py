def solution(answers):
    answer = []

    std1 = [1, 2, 3, 4, 5]
    std2 = [2, 1, 2, 3, 2, 4, 2, 5]
    std3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    records = [0, 0, 0]

    for i in range(0, len(answers)):
        if answers[i] == std1[i % 5]:
            records[0] += 1
        if answers[i] == std2[i % 8]:
            records[1] += 1
        if answers[i] == std3[i % 10]:
            records[2] += 1

    top = max(records)
    for i in range(0, len(records)):
        if records[i] == top:
            answer.append(i + 1)

    return answer