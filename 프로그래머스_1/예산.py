#https://programmers.co.kr/learn/courses/30/lessons/12982
def solution(d, budget):
    answer = 0
    d.sort()
    max = 0
    i = 0
    while (i<len(d)):
        if max + d[i] > budget:
            break
        else:
            max += d[i]
            i += 1
    answer=i
    return answer