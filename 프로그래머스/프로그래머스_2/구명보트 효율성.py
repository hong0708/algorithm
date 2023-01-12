#https://programmers.co.kr/learn/courses/30/lessons/42885
#정렬 후에 무거운사람 먼저 타지만 가벼운 사람이 같이 탈 수 있으면 answer -1
def solution(people, limit):
    people.sort()
    people.reverse()

    answer = len(people)

    light = len(people) - 1
    heavy = 0
    while heavy < light:
        if people[heavy] + people[light] <= limit:
            light -= 1
            answer -= 1
        heavy += 1
    return answer
