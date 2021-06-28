# 두 배열의 원소 교체

# 두 개의 배열 A와 B가 있고 N개의 원소로 구성되어 있다.
# 최대 K번 바꿔치기 연산을 수행할 때 바꿔치기란 배열 A에 있는 원소 하나와 배열 B에 있는 원소 하나를 골라서 두 원소를 서로 바꾸는 것을 말한다.
# 최종 목표는 배열 A의 모든 원소의 합이 최대가 되도록 하는 것이다.

# 입력 에시
# 5 3
# 1 2 5 4 3
# 5 5 6 6 5

# 출력 예시
# 26

# 원소의 갯수, 교환할 갯수
n, k = map(int, input().split())

# 배열 2개 입력 받기
array1 = list(map(int, input().split()))
array2 = list(map(int, input().split()))

# 작은 순서대로, 큰 순서대로 정렬
array1.sort()
array2.sort(reverse=True)

# 배열 간 교환
for i in range(k):
    if (array1[i] < array2[i]):
        array1[i], array2[i] = array2[i], array1[i]
    else:
        pass

print(sum(array1))