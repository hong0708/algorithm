def solution(progresses, speeds):
    answer = []
    day = 0
    count = 0
    while len(progresses) > 0:
        if progresses[0] + speeds[0] * day >= 100:
            count += 1
            progresses.pop(0)
            speeds.pop(0)
        elif progresses[0] + speeds[0] * day < 100 and count > 0:
            answer.append(count)
            count = 0
            day += 1
        else:
            day += 1
    answer.append(count)
    return answer
