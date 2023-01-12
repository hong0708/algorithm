#https://programmers.co.kr/learn/courses/30/lessons/42577
#처음에 접두가 아닌 포함으로 이해해서 고생함;
def solution(phone_book):
    answer = True
    for i in range(len(phone_book)):
        for j in range(i + 1, len(phone_book)):
            if len(phone_book[i]) > len(phone_book[j]):
                if phone_book[i].startswith(phone_book[j]):
                    answer =False
                    break

            else:
                if phone_book[j].startswith(phone_book[i]):
                    answer =False
                    break

        if answer == False:
            break
    return answer