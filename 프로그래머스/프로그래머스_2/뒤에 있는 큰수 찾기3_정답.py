def solution(numbers):
    answer = [-1 for _ in range(len(numbers))]
    # 값, 위치 저장
    impl = []

    for i in range(len(numbers)):
        if impl:
            while impl:
                if numbers[impl[-1]] < numbers[i]:
                    answer[impl[-1]] = numbers[i]
                    impl.pop()
                else:
                    break
        impl.append(i)
    return answer
