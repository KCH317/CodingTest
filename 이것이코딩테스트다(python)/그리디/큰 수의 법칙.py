# 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
# M이 8이고 K가 3이라고 한다면 8개의 수를 써서 가장 큰 수를 만들어야 하며 연속된 수가 3번까지만 가능하다는 뜻이다.

# 입력
# 5 8 3
# 2 4 5 4 6

# 출력
# 46

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0: 
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)