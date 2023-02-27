def solution(lines):
    answer = 0
    temp = [0 for _ in range(404)]
    for i in range(len(lines)):
        for j in range(lines[i][0] * 2, lines[i][1] * 2 + 1):
            temp[j + 202] += 1
    line = 0
    start = 0
    for k in range(404):
        if temp[k] > 1:
            line += 1
            start = 1
        if start != 0 and temp[k] < 2:
            answer += (line - 1) // 2
            start, line = 0, 0
    return answer