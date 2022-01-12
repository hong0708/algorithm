#https://programmers.co.kr/learn/courses/30/lessons/70129
#전에 봤던 문제 그당시에 못풀었던가 오래 걸렸는데 금방 해결
def solution(s):
    answer=[]
    count = 0
    play = 0
    while len(s) != 1:
        play += 1
        while s.count('0'):
            count += s.count("0")
            sub = s.replace('0', '')
            s = sub
        a = bin(len(s))
        s = a[2:]
    answer.append(play)
    answer.append(count)
    return answer