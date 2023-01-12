#https://programmers.co.kr/learn/courses/30/lessons/12941
def solution(A,B):
    answer = 0
    A.sort()
    B.sort()
    for i in range(len(A)):
        answer += (A[i]*B[-(i+1)])
    return answer