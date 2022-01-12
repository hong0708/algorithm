#https://programmers.co.kr/learn/courses/30/lessons/12939
#split으로 구분 후에 리스트를 만드는데 map을 이용해 인트형으로 다 바꿈
def solution(s):
    answer = ''
    num = s.split(' ')
    num = list(map(int, num))

    answer = ''
    answer += str(min(num))
    answer += ' '
    answer += str(max(num))
    return answer