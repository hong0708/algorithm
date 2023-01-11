# 이미 본 주제 노래들 지우기
def erase(gen, t):
    temp = []
    for i in range(len(gen)):
        if gen[i] == t:
            temp.append('')
        else:
            temp.append(gen[i])
    return temp


# 다음 장르 찾기
def find(gen):
    for i in range(len(gen)):
        if gen[i] != '':
            return gen[i]


# 장르 남은거 있는지 확인하고 없으면 종료
def check(gen):
    for i in range(len(gen)):
        if gen[i] != '':
            return True
    return False


def solution(genres, plays):
    answer = []

    a_loc = []
    b_loc = []

    contin = True

    while contin:

        loc = []
        count = []

        title = find(genres)
        sum_count = 0
        # 해당 장르 노래들 전체 들은 횟수와 최대 횟수 2개 뽑기
        for i in range(len(genres)):
            # 해당 주제
            if title == genres[i]:
                sum_count += plays[i]

                # 0개일때 그냥 추가 1개일때 비교해서 추가
                if len(loc) == 0:
                    loc.append(i)
                    count.append(plays[i])
                elif len(loc) == 1:
                    if count[0] > plays[i]:
                        loc.append(i)
                        count.append(plays[i])
                    else:
                        loc = [i] + loc
                        count = [plays[i]] + count
                # 추가 할 상황인지 확인하고 제일 큰거랑 비교해서 추가하기
                else:
                    if count[1] < plays[i]:
                        count.pop()
                        loc.pop()
                        if count[0] < plays[i]:
                            loc = [i] + loc
                            count = [plays[i]] + count
                        else:
                            loc.append(i)
                            count.append(plays[i])

        genres = erase(genres, title)
        contin = check(genres)
        b_loc.append(sum_count)
        a_loc.append(loc)

    while b_loc:
        temp_loc = b_loc.index(max(b_loc))
        answer += a_loc[temp_loc]
        a_loc.pop(temp_loc)
        b_loc.pop(temp_loc)

    return answer
