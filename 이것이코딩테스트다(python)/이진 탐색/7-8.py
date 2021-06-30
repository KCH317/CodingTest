# 떡볶이 떡 만들기

# 첫째 줄에 떡의 개수 N과 요청한 떡의 길이 M이 주어진다.
# 둘째 줄에는 떡의 개별 높이가 주어진다.
# 떡 높이의 총합은 항상 M 이상이므로, 손님은 필요한 양만큼 떡을 사갈 수 있다.
# 적어도 M만큼의 떡을 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.

# 입력 예시
# 4 6
# 19 15 10 17

# 출력 예시
# 15


# 떡의 개수(N)와 요청한 떡의 길이(M)을 입력받기
n, m = map(int, input().split())

# 각 떡의 길이 입력받기
array = list(map(int, input().split()))

# 이진 탐색
start = 0
end = max(array)

result = 0
while start <= end:
    mid = (start + end) // 2
    total = 0
    for x in array:
        # 떡을 잘랐을 때 길이
        if x > mid:
            total += x - mid
    
    # 떡의 양이 부족한 경우 더 많이 짜르기 (왼쪽 부분 탐색)
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
        
print(result)