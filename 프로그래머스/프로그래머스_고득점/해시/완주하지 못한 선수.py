def solution(participant, completion):
    answer = ""
    participant = sorted(participant)
    completion = sorted(completion)
    for i in range(len(completion)):
        if completion[i] != participant[i]:
            answer = participant[i]
            break
    if answer == "":
        answer = participant[-1]
    return answer