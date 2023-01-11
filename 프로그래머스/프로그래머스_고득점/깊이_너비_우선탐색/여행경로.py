visited = []  # 티켓별로 사용했는지를 체크하기 위한 리스트
answer = []  # 경로를 담아두는 리스트
ticket = []  # 입력으로 받은 티켓을 전역 리스트로


# (사용한 티켓의 개수, 전체 티켓의 개수, dfs를 돌면서 담아둔 여행 경로, 출발 도시)
def dfs(cnt, n, ans, city):
    # 전체 티켓을 다 사용했으면 현재 경로가 기존에 찾았던 경로보다 알파벳 순으로 앞서는지를 체크
    # 앞선다면 경로를 변경해준다.
    if cnt == n:
        global answer

        if not ans > answer or len(answer) == 0:
            answer = ans
        return

    for i in range(n):
        if visited[i] or ticket[i][0] != city:
            continue

        if ticket[i][0] == city:
            visited[i] = True
            dfs(cnt + 1, n, ans + [ticket[i][1]], ticket[i][1])
            visited[i] = False


def solution(tickets):
    global visited, ticket
    visited = [False for _ in range(len(tickets))]
    ticket = tickets[:]

    dfs(0, len(tickets), ['ICN'], 'ICN')
    return answer
