from collections import deque


def solution(begin, target, words):
    if target not in words:
        # 애초에 words리스트에 target값이 없다면 return 0
        return 0

    q = deque()
    q.append([begin, 0])

    while q:
        x, cnt = q.popleft()

        if x == target:
            return cnt
            # target값이 되면 cnt 출력

        for i in range(0, len(words)):
            diff = 0
            word = words[i]
            for j in range(len(x)):
                if x[j] != word[j]:
                    diff += 1
            if diff == 1:
                q.append([word, cnt + 1])
    return 0
    # target값이 있으나 변환될 수 없다면
