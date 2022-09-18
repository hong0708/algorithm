def solution(survey, choices):
    answer = ''
    check_dict = {'R': 0, 'T': 0, 'F': 0, 'C': 0, 'M': 0, 'J': 0, 'A': 0, 'N': 0}
    for idx, question in enumerate(survey):
        if choices[idx] == 4:
            continue
        elif choices[idx] - 4 < 0:
            check_dict[question[0]] += abs(choices[idx] - 4)
        else:  
            check_dict[question[1]] += abs(choices[idx] - 4)

    if check_dict['R'] >= check_dict['T']:
        answer += 'R'
    else:
        answer += 'T'
    if check_dict['C'] >= check_dict['F']:
        answer += 'C'
    else:
        answer += 'F'
    if check_dict['J'] >= check_dict['M']:
        answer += 'J'
    else:
        answer += 'M'
    if check_dict['A'] >= check_dict['N']:
        answer += 'A'
    else:
        answer += 'N'

    return answer