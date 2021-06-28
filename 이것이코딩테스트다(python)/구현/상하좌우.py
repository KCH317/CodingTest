# NxN 크기의 정사각형 공간 (가장 왼쪽 위 좌표는 (1,1)), 시작좌표 (1,1)
# L : 왼쪽으로 한 칸 이동
# R : 오른쪽으로 한 칸 이동
# U : 위로 한 칸 이동
# D : 아래로 한 칸 이동

# 계획서가 주어졌을 때 여행가 A가 최종적으로 도착할 지점의 좌표를 출력하는 프로그램을 작성하시오.

# 입력
# 5
# R R R U D D

# 출력
# 3 4

n = int(input())
data = input().split()

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

x, y = 1, 1

move = ['L', 'D', 'R', 'U']

for i in data:
    for j in range(len(move)): 
        if move[j] == i:
            xx = x + dx[j]
            yy = y + dy[j]
    if xx < 1 or xx > n or yy < 1 or yy > n:
        continue
    x = xx
    y = yy

print(x, y)