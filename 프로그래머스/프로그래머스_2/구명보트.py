#https://programmers.co.kr/learn/courses/30/lessons/42885
#max min으로 쉽게 해결했지만 효율성 탈락
# 아마 min max 자체가 오래 걸리는거 같음
def solution(people, limit):
    answer = 0
    total = 0
    while True:
        if not people:
            break
        elif len(people) == 1:
            answer += 1
            people = []
        elif max(people) + min(people) <= limit:
            answer += 1
            people.remove(max(people))
            people.remove(min(people))
        elif max(people) + min(people) > limit:
            answer += 1
            people.remove(max(people))
    return answer