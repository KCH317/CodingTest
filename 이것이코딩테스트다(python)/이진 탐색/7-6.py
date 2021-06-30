# 부품 찾기 (계수 정렬)

# 전자 매장에는 부품 N개가 있따. 각 부품은 정수 형태의 고유한 번호가 있다.
# 어느 날 손님이 M개 종류의 부품을 대량으로 구매하겠다며 당일 날 견적서를 요청했다.

# 가게의 부품이 총 5개일 때 부품 번호
# N = 5
# [8, 3, 7, 9, 2]

# 손님은 총 3개의 부품이 있는지 확인 요청, 요청한 부품 번호
# M = 3
# [5, 7, 9]

# 이때 손님이 요청한 부품 번호의 순서대로 부품을 확인해 부품이 있으면 yes, 없으면 no를 출력한다.

# 일력 예시
# 5
# 8 3 7 9 2 
# 3
# 5 7 9

# 출력 예시
# no yes yes


# N(가게의 부품 수 입력)
n = int(input())
array1 = [0] * 1000001
# 부품의 번호
for i in input().split():
    array1[int(i)] = 1

# M(손님이 원하는 부품 개수 입력)
m = int(input())
# 손님이 원하는 부품 번호
array2 = list(map(int, input().split()))

for target in array2:
    if array1[target] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')