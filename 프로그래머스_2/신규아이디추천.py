#https://programmers.co.kr/learn/courses/30/lessons/72410
#더럽다 코드가
def solution(new_id):
    answer = ''
    new_id_1 = ""

    for i in range(len(new_id)):
        if new_id[i].isupper():
            new_id_1 += new_id[i].lower()

        if new_id[i].isdigit():
            new_id_1 += new_id[i]
        if new_id[i].islower():
            new_id_1 += new_id[i]
        if new_id[i] == "-":
            new_id_1 += new_id[i]
        if new_id[i] == "_":
            new_id_1 += new_id[i]

        if new_id[i] == ".":
            if len(new_id_1) == 0:
                pass
            elif new_id_1[len(new_id_1) - 1] == ".":
                pass
            else:
                new_id_1 += new_id[i]

    if len(new_id_1) == 0:
        new_id_1 += "a"

    if new_id_1[len(new_id_1) - 1] == ".":
        new_id_1 = new_id_1[:len(new_id_1) - 1]

    if len(new_id_1) > 15:
        new_id_1 = new_id_1[:15]
        if new_id_1[14] == ".":
            new_id_1 = new_id_1[:14]

    new_id_2 = new_id_1[-1]
    while len(new_id_1) < 3:
        new_id_1 += new_id_2
    answer = new_id_1
    return answer