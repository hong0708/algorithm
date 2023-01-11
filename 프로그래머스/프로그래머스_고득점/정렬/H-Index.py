def solution(citations):
    answer = 0
    total = len(citations)
    citations = sorted(citations)

    for i in range(total - 1, -1, -1):
        if i == total - 1:
            if citations[i] >= 1 and total - 1 <= 1:
                answer = max(answer, 1)
        else:
            # h 큰값부터 확인해서 가능하면 정답과 비교
            for h in range(citations[i], -1, -1):
                if i + 1 <= h and total - i >= h:
                    answer = max(answer, h)
                    if h == citations[i]:
                        return answer
    return answer
