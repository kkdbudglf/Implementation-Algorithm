# n 입력 받기
n = int(input())
x, y = 1, 1
plans = input().split()  # R R R U D D

# L, R, U, D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# plans 하나씩 대입
for plan in plans:  # R
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 정사각형 공간을 벗어나는지 확인
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny
print(x, y)
