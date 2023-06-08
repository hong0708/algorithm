def check(w, arr):
    ans = 0

    # 양쪽 대각
    for i in range(0, 3):
        if arr[i][i] != w:
            ans = 0
            break
        else:
            ans += 1
            if ans == 3:
                return True

    for i in range(0, 3):
        if arr[2 - i][i] != w:
            ans = 0
            break
        else:
            ans += 1
            if ans == 3:
                return True

    # 직선 방향
    for i in range(0, 3):
        for j in range(0, 3):
            if arr[i][j] != w:
                ans = 0
                break
            else:
                ans += 1
                if ans == 3:
                    return True

        for j in range(0, 3):
            if arr[j][i] != w:
                ans = 0
                break
            else:
                ans += 1
                if ans == 3:
                    return True


def count(w, arr):
    ans = 0
    for i in range(3):
        for j in range(3):
            if arr[i][j] == w:
                ans += 1
    return ans


def solution(board):
    answer = 0

    o_count = count('O', board)
    x_count = count('X', board)
    o_check = check('O', board)
    x_check = check('X', board)

    if x_count == o_count or x_count + 1 == o_count:

        # o의 개수가 많거나 같가 때문에 최대 개수임 즉 o개수가 3개 이상이면 끝났을지도 모름
        if o_count >= 3:

            # 둘다 3연속일 수 없음
            if o_check and x_check:
                return answer

            # o만 3연속이 존재
            elif o_check:

                # o만 연속인데 x가 하나 더 적어야함
                if o_count != x_count + 1:
                    return answer

            # x만 3연속 존재
            elif x_check:

                # x가 끝냈으니 개수 꼭 같아야함
                if o_count != x_count:
                    return answer
    else:
        return answer

    return 1
