# 큐 예제
#  삽입(5) 삽입(2) 삽입(3) 삽입(7) 삭제() 삽입(1) 삽입(4) 삭제()

from typing import Deque


queue = Deque() # deque 라이브러리 사용

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 들어있는 순서
queue.reverse() # 역순
print(queue) # 출력될 순서