#https://programmers.co.kr/learn/courses/30/lessons/42746
# 람다 키 맵 이용
#3번하는이유 자리수 때문에
#처음엔 복잡하게 생각했는데 람다랑 키가 생각났음 리버스의 경우 나중에 참고하여 추가함
#개인적으로 좀 뿌듯
def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)

    a = False

    for i in range(len(numbers)):
        if numbers[i] != '0':
            a = True
    if a:
        answer = str(''.join(numbers))

    else:
        answer = '0'

    return answer