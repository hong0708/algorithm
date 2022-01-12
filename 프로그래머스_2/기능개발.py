#https://programmers.co.kr/learn/courses/30/lessons/42586
#pop이용하여 맨앞만 제거해감
def solution(progresses, speeds):
    answer = []
    day = 0
    count = 0
    while len(progresses) > 0:
        #맨앞이 100이 넘는 경우
        if progresses[0] + speeds[0] * day >= 100:
            count += 1
            progresses.pop(0)
            speeds.pop(0)
        #100이 넘는것을 제거해주고 없으면 count 즉 100이 넘어 빠진게 있는지 확인하고 답에 추가
        elif progresses[0] + speeds[0] * day < 100 and count > 0:
            answer.append(count)
            count = 0
            day += 1
        # 맨 앞이 100이 안넘고 count가 0이어서 day만 지나가는 경우
        else:
            day += 1
    answer.append(count)
    # 마지막 count가 추가 되어야해서 추가
    return answer