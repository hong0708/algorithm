def solution(num, total):
    middle_idx = num // 2

    middle_num = total // num

    start_num = middle_idx * - 1 if num % 2 == 1 else middle_idx * -1 + 1
    end_num = middle_idx + 1

    answer = [num + middle_num for num in range(start_num, end_num)]

    return answer
