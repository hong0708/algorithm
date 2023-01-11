def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)

    a = False

    for i in range(len(numbers)):
        if numbers[i] != '0':
            a = True
    if a:
        answer = str(''.join(numbers))

    else:
        answer = '0'

    return answer
