from collections import deque

n, k = map(int, input().split())
belt = deque(list(map(int, input().split())))
robot = deque([0] * n)
answer = 0

while 1:
    belt.rotate(1)
    robot.rotate(1)
    robot[-1] = 0  # 로봇 배열 마지막이니깐 로봇이 내려가는 부분이니 0으로
    if sum(robot):  # 로봇이 남으면
        for i in range(n - 2, -1, -1):  # 로봇 내려가는 부분 인덱스 i-1 이므로 그 전인 i-2부터 확인
            if robot[i] == 1 and robot[i + 1] == 0 and belt[i + 1] >= 1:
                robot[i + 1] = 1
                robot[i] = 0
                belt[i + 1] -= 1
        robot[-1] = 0  # 로봇 배열 마지막이니깐 이 부분도 로봇 out -> 0임
    if robot[0] == 0 and belt[0] >= 1:
        robot[0] = 1
        belt[0] -= 1
    answer += 1  # 다돌고 +1
    if belt.count(0) >= k:
        break
print(answer)
