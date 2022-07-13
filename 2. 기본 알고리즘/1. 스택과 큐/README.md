# 가장 기본이 되는 자료구조 : 스택과 큐



## 1. 스택 자료구조

<img src="C:\Users\여름\Desktop\학습자료\이러닝\[큐레이팅# 플러스] 최적의 코딩을 결정하는 기본 알고리즘\image\1-1.PNG" alt="1-1" style="zoom: 67%;" />

* 먼저 들어 온 데이터가 나중에 나가는 형식(선입후출)의 자료구조



## 스택 구현 예제

```python
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1]) # 최상단 원소부터 출력
print(stack) # 최하단 원소부터 출력

#실행결과
#[1,3,2,5]
#[5,2,3,1]
```



## 2. 큐 자료구조

![1-2](C:\Users\여름\Desktop\학습자료\이러닝\[큐레이팅# 플러스] 최적의 코딩을 결정하는 기본 알고리즘\image\1-2.PNG)

* 먼저 들어 온 데이터가 먼저 나가는 형식(선입선출)의 자료구조



## 큐 구현 예제

```python
from collections import deque

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
# 리스트 메소드만 사용할 수 있지만 시간 복잡도로 인해 deque 라이브러리 사용

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse() # 역순으로 바꾸기
print(queue) # 나중에 들어온 원소부터 출력

#실행결과
#deque([3,7,1,4])
#deque([4,1,7,3])
```

