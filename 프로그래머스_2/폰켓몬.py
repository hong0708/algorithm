#https://programmers.co.kr/learn/courses/30/lessons/1845
def solution(nums):
    answer = 0
    a = len(nums) // 2
    num = set(nums)
    if a > len(num):
        answer = len(num)
    else:
        answer = a
    return answer