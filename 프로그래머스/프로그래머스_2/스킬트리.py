#https://programmers.co.kr/learn/courses/30/lessons/49993
#순열 조합이용
from itertools import combinations
def solution(skill, skill_trees):
    answer = len(skill_trees)
    for i in range(len(skill_trees)):
        case = []
        for j in range(len(skill_trees[i])):
            if skill_trees[i][j] in skill:
                case.append(skill_trees[i][j])

        for a in range(len(case)):
            if case[a] != skill[a]:
                answer -= 1
                break
    return answer