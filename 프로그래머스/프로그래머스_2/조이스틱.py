alpa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
        'W', 'X', 'Y', 'Z']


def count(word):
    where = alpa.index(word)
    if where > 12:
        where -= 26
        where *= -1
    return where


def solution(name):
    answer = 0

    # 각 문자의 다음, 이전 알파벳으로의 이동
    change = []

    # 위치 이동 합 구할 변수 초기는 순차적으로 움직일 때의 값으로 한다.
    minCount = len(name) - 1

    for i in range(len(name)):
        change.append(count(name[i]))

        # 연속 a 찾기
        nextIdx = i + 1
        while nextIdx < len(name):
            if name[nextIdx] == 'A':
                nextIdx += 1
            else:
                break

        # 기존, 연속된 A의 왼쪽시작 방식, 연속된 A의 오른쪽시작 방식 비교 및 갱신
        # 왼쪽 시작의 경우 지금 위치까지 가고 돌아가서 반대로
        # 오른쪽 시작의 경우 뒤에서 갔다가 뒤로 다시오고 i 까지 가야함
        minCount = min(minCount, (2 * i) + len(name) - nextIdx, i + (2 * (len(name) - nextIdx)))

    answer += sum(change)
    answer += minCount

    return answer
