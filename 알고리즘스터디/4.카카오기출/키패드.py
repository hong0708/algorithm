def solution(numbers, hand):
    answer = ''
    key = {1: [0, 0], 2: [0, 1], 3: [0, 2],
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           '*': [3, 0], 0: [3, 1], '#': [3, 2]}

    # 시작 위치
    left_loc = key['*']
    right_loc = key['#']

    for i in range(len(numbers)):
        now_loc = key[numbers[i]]

        # 1, 4, 7을 누르는 경우 무조건 왼손
        if numbers[i] in [1, 4, 7]:
            answer += 'L'
            left_loc = now_loc

        # 3, 6, 9를 누르는 경우 무조건 오른손
        elif numbers[i] in [3, 6, 9]:
            answer += 'R'
            right_loc = now_loc

        else:
            left_dis = 0
            right_dis = 0

            left_dis += abs(left_loc[0] - now_loc[0]) + abs(left_loc[1] - now_loc[1])
            right_dis += abs(right_loc[0] - now_loc[0]) + abs(right_loc[1] - now_loc[1])

            if left_dis < right_dis:
                answer += 'L'
                left_loc = now_loc

            elif left_dis > right_dis:
                answer += 'R'
                right_loc = now_loc

            else:
                if hand == 'left':
                    answer += 'L'
                    left_loc = now_loc

                else:
                    answer += 'R'
                    right_loc = now_loc

    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
