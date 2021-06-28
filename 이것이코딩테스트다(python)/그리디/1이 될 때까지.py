# 1이 될 때까지
# 입력예시
# N = 17, K = 4
# 출력예시
# 3

# 1. N에서 1을 뺀다.
# 2. N을 K로 나눈다.

n, k = map(int, input().split())
count = 0
while True:
    if n != 1:
        if n % k == 0:
            count += 1
            n /= k
        else:
            count += 1
            n -= 1
    else:
        break
print(count)