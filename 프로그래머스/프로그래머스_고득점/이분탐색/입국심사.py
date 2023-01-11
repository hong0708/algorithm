# a = n 개 이하 값만 계산
def check(t, l, a):
    ans = 0
    for i in l:
        ans += t // i
        if ans > a:
            ans = a + 1
            break
    return ans


def solution(n, times):
    answer = 0
    num = min(times)
    end = num * n
    start = 0

    while start <= end:
        mid = (end + start) // 2

        if n <= check(mid, times, n):
            if n > check(mid - 1, times, n):
                answer = mid
                break
            else:
                end = mid - 1

        elif n > check((end + start) // 2, times, n):
            start = mid + 1

    return answer
