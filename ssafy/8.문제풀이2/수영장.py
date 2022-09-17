def route(now_fee, now_month):
    global min_fee

    if now_fee > min_fee:
        return

    if all(visited) :
        if min_fee >= now_fee:
            min_fee = now_fee
        return

    else:
        if year_data[now_month] == 0:
            visited[now_month] = True
            route(now_fee, now_month + 1)
            visited[now_month] = False
        else:
            for i in range(3):
                if i == 0:
                    visited[now_month] = True
                    route(now_fee + year_data[now_month] * fee[i], now_month + 1)
                    visited[now_month] = False
                elif i == 1:
                    visited[now_month] = True
                    route(now_fee + fee[i], now_month + 1)
                    visited[now_month] = False
                else:
                    count = 0
                    for t in range(now_month, now_month + 3):
                        if t == 12:
                            visited[t] = True
                            count += 1
                            break
                        visited[t] = True
                        count += 1
                    route(now_fee + fee[i], now_month + count)
                    count = 0
                    for c in range(now_month, now_month + 3):
                        if c == 12:
                            visited[c] = False
                            break
                        visited[c] = False


t = int(input())
for tc in range(t):
    fee = list(map(int, input().split()))
    year_data = [0] + list(map(int, input().split()))
    min_fee = fee[3]
    visited = [True] + [False] * 12
    route(0, 1)
    print("#{} {}".format(tc + 1, min_fee))
