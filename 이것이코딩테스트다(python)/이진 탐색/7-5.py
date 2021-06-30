# 부품 찾기 (이진 탐색)

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

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        # 타겟을 찾은 경후
        if array[mid] == target:
            return mid
        # 타겟이 mid보다 작은 경우
        elif array[mid] > target:
            end = mid - 1
        # 타겟이 mid보다 큰 경우
        else:
            start = mid + 1

    return None
    
# N(가게의 부품 수 입력)
n = int(input())
# 부품의 번호
array1 = list(map(int, input().split()))

# M(손님이 원하는 부품 개수 입력)
m = int(input())
# 손님이 원하는 부품 번호
array2 = list(map(int, input().split()))

array1.sort() # 이진 탐색을 위한 정렬

for target in array2:
    result = binary_search(array1, target, 0, n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')