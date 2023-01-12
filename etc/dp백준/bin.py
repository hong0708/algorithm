def solution(numbers):
    answer = []
    for i in numbers:
        abc = list(bin(i))
        a = 1
        while True:
            if abc[-a] == '0':
                break
            elif a == len(abc) - 1:
                break
            a += 1
        if a > 2:
            answer.append(i + 2 ** (a - 2))
        else:
            answer.append(i + 1)

    return answer


numbers = [4, 12, 3, 7, 15, 12, 31, 63]
print(solution(numbers))
#프로그래머스 월간코테 2번 문제