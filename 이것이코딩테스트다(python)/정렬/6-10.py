# 위에서 아래로

# 큰 수부터 작은 수의 순서로 정렬하라
# 첫째 줄에 수열에 속해 있는 수의 개수 N이 주어진다.
# 둘째 줄부터 N+1번째 줄까지 N개의 수가 입력된다.

# 입력 예시
# 3
# 15
# 27
# 12

# 출력 예시
# 27 15 12

# N을 입력받기
n = int(input())

# 수열 받기
array = []
for i in range(n):
    array.append(int(input()))

# 정렬
array.sort(reverse=True)

for i in array:
    print(i, end=' ')