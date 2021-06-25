# 음료수 얼려 먹기
# N x M 크기의 얼음 틀이 있다.
# 구멍이 뚫려 있는 부분은 0, 칸만이가 존재하는 부분은 1로 표시된다.
# 한 번에 만들 수 있는 아이스크림의 개수를 출력한다.

# 입력 예시
# 4 5
# 00110
# 00011
# 11111
# 00000

# 출력 예시
# 3

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x,y):
    # 범위 검증
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

# 아이스크림 개수 구하기
cnt = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            cnt += 1

print(cnt)