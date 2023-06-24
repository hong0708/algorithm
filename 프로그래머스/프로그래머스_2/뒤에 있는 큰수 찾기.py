def solution(numbers):
    answer = []
    for i in range(len(numbers) - 1):
        ex = False
        for j in range(i + 1, len(numbers)):
            if numbers[i] < numbers[j]:
                answer.append(numbers[j])
                ex = True
                break
        if not ex:
            answer.append(-1)

    return answer +[-1]