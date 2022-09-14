def solution(n, left, right):
    answer = []

    if left < n:
        x = 0
        y = left
    else:
        x = left // n
        y = left % n

    count = 0

    for a in range(x, n):
        if a == x:
            for b in range(y, n):
                count += 1
                w = max(a, b) + 1
                answer.append(w)
                if count == right - left + 1:
                    break
        else:
            for z in range(0, n):
                count += 1
                w = max(a, z) + 1
                answer.append(w)
                if count == right - left + 1:
                    break
        if count == right - left + 1:
            break
    return answer


print(solution(3, 2, 5))
print(solution(4, 7, 14))
