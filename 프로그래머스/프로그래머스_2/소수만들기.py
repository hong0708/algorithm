#https://programmers.co.kr/learn/courses/30/lessons/12977
#combinations 활용
from itertools import combinations
def solution(nums):
    case = list(combinations(nums,3))
    answer = len(case)
    for i in range(len(case)):
        total = case[i][0]+case[i][1]+case[i][2]
        for j in range(2,total):
            if total % j == 0:
                answer -= 1
                break

    return answer