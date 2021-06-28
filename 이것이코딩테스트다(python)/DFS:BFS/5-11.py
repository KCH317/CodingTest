# 미로 탈출
# N x M 미로
# 괴물이 있는 곳은 0, 괴물이 없는 곳은 1
# 시작 위치는 항상 1,1이다.
# 미로를 탈출하는 최소 칸의 개수를 구하여라

# 입력 예시
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111

# 출력 예시
# 10


from collections import deque

# 입력 정보 받기
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 좌 상 우 하
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        # print(x,y)
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if xx < 0 or xx >= n or yy < 0 or yy >= m:
                continue

            if graph[xx][yy] == 0:
                continue

            if graph[xx][yy] == 1:
                graph[xx][yy] = graph[x][y] + 1
                queue.append((xx,yy))
                
    return graph[n-1][m-1]

print(bfs(0,0))