def solution(k, d):
    count = 0

    if d % k == 0:
        y = d
    else:
        y = d - d % k
    x = 0

    while x <= d:
        # 해당 점이 가능하면 아래 y점 모두 포함
        if x ** 2 + y ** 2 <= d ** 2:
            count += y // k + 1
            x += k
        # 넘어가면 y 값 줄이기
        else:
            y -= k
    return count
