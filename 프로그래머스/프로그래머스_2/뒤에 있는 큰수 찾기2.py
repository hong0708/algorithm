def solution(numbers):
    answer = []
    max_num = numbers[-1]
    max_loc = len(numbers) - 1
    for i in range(len(numbers) - 2, -1, -1):
        if numbers[i] >= max_num:
            answer = [-1] + answer
            max_num = numbers[i]
            max_loc = i
        else:
            for j in range(i+1, max_loc + 1):
                if numbers[i] < numbers[j]:
                    answer = [numbers[j]] + answer
                    break

    return answer + [-1]
