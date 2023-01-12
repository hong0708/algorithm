#https://programmers.co.kr/learn/courses/30/lessons/17681
# zip활용을 통해 반복문에서 배열 두개 각각 꺼내서 활용가능
# bin으로 2진법으로 바꿔준다 하지만 앞에 0b(이진법을 뜻하는)이 추가됨
def solution(n, arr1, arr2):
    answer = []
    for decimal1, decimal2 in zip(arr1, arr2):
        binary12 = str(bin(decimal1 | decimal2))[2:]
        binary12 = '0' * (n - len(binary12)) + binary12
        binary12 = binary12.replace('1', '#')
        binary12 = binary12.replace('0', ' ')
        answer.append(binary12)
    return answer