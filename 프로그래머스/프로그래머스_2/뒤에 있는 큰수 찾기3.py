from collections import deque


def solution(numbers):
    answer = [-1 for _ in range(len(numbers))]
    # 값, 위치 저장
    impl = deque()
    min_num = 1000000

    for i in range(len(numbers)):
        if impl:
            if min_num >= numbers[i]:
                impl.append([numbers[i], i])
            else:
                for _ in range(len(impl)):
                    now = impl.popleft()
                    if now[0] < numbers[i]:
                        answer[now[1]] = numbers[i]
                    else:
                        impl.append(now)
                impl.append([numbers[i], i])
        else:
            impl.append([numbers[i], i])

        min_num = min(min_num, numbers[i])

    return answer
