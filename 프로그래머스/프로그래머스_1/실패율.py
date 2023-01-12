#https://programmers.co.kr/learn/courses/30/lessons/42889
# .count(a) a의 개수를 측정 이걸 이용한 것이 가장 컸던 거 같다
def solution(N, stages):
    answer = []
    percent = [0 for i in range(N)]

    level = len(stages)

    for i in range(len(percent)):
        if level != 0:
            percent[i] = stages.count(i + 1) / level
            level -= stages.count(i + 1)

    for i in percent:
        print(i)

    while (True):
        max = 0
        where = 0
        for i in range(N):
            if i == 0:
                max = percent[i]
            if max < percent[i]:
                max = percent[i]
                where = i
        percent[where] = -1
        answer.append(where + 1)
        if len(answer) == N:
            break

    return answer