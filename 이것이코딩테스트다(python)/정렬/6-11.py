# 성적이 낮은 순서로 학생 출력하기
# N명의 학생 정보가 있다.
# 학생정보는 학색의 이름과 학생의 성적으로 구분된다.
# 각 학생의 이름과 성적 정보가 주어졌을 때 성적이 낮은 순서대로 학생의 이름을 출력하는 프로그램을 작성하시오.

# 첫 번째 줄에 학생의 수 N이 입력된다.
# 두 번째 줄부터 N + 1 번째 줄에는 학생의 이름을 나타내는 문자열 A와 학생의 성적을 나타내는 정수 B가 공백으로 구분되어 입력된다

# 입력 예시
# 2
# 홍길동 95
# 이순신 77

# 출력 예시
# 이순신 홍길동

# 학생 수 N
n = int(input())

# 학생 정보
array = []
for i in range(n):
    data = input().split()
    array.append((data[0], int(data[1])))

array.sort(key=lambda age: age[1])

for i in array:
    print(i[0], end=" ")