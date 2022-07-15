# 우선순위에 따라 데이터를 꺼내는 자료구조



## 우선순위 큐(Priority Queue)

* 우선순위 큐는 우선 순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조
* 우선순위 큐는 데이터를 우선순위에 따라 처리하고 싶을 때 사용합니다.
  * 예시) 물건 데이터를 자료구조에 넣었다가 가치가 높은 물건부터 꺼내서 확인해야하는 경우

<img src="C:\Users\여름\Desktop\학습자료\이러닝\[큐레이팅# 플러스] 최적의 코딩을 결정하는 기본 알고리즘\image\2-1.PNG" alt="2-1" style="zoom: 67%;" />

* 우선순위 큐를 구현하는 방법은 다양합니다.

  * 단순히 리스트를 이용한 방법
  * 힙(heap) 을 이용한 방법

* 방법에 따른 시간 복잡도

  <img src="C:\Users\여름\Desktop\학습자료\이러닝\[큐레이팅# 플러스] 최적의 코딩을 결정하는 기본 알고리즘\image\2-2.PNG" alt="2-2" style="zoom:67%;" />

  * 단순히 N개의 데이터를 힙에 넣었다가 모두 꺼내는 작업은 정렬과 동일합니다(힙 정렬)
  * 이 경우 시간 복잡도는 O(NlogN)



## 힙(Heap)의 특징

* 힙은 완전 이진 트리 자료구조의 일종
* 힙에서는 항상 **루트 노트(root node)**를 제거.
* 최소 힙(min heap)
  * 루트 노드가 가장 작은 값을 가집니다.
  * 따라서 값이 작은 데이터가 우선적으로 제거
* 최대 힙(max heap)
  * 루트 노드가 가장 큰 값을 가집니다.
  * 따라서 값이 큰 데이터가 우선적으로 제거됩니다.

<img src="C:\Users\여름\Desktop\학습자료\이러닝\[큐레이팅# 플러스] 최적의 코딩을 결정하는 기본 알고리즘\image\2-3.PNG" alt="2-3" style="zoom:50%;" />



## 완전 이진 트리 (Complete Binary Tree)

* 완전 이진 트리란 루트 노드부터 시작하여 왼쪽 자식 노드, 오른쪽 자식 노드 순서대로 데이터가 차례대로 삽입되는 트리를 의미합니다.

![2-4](C:\Users\여름\Desktop\학습자료\이러닝\[큐레이팅# 플러스] 최적의 코딩을 결정하는 기본 알고리즘\image\2-4.PNG)

## 최소 힙 구성 함수: Min-Heapify()

* (상향식) 부모 노드로 거슬러 올라가며, 부모보다 자신의 값이 더 작은 경우에 위치를 교체합니다.

![2-5](C:\Users\여름\Desktop\학습자료\이러닝\[큐레이팅# 플러스] 최적의 코딩을 결정하는 기본 알고리즘\image\2-5.PNG)



## 힙에 새로운 원소가 삽입될 때

* 새로운 원소가 삽입되었을때, O(logN)의 시간 복잡도로 힙 성질을 유지하도록 할 수 있습니다.

![2-6](C:\Users\여름\Desktop\학습자료\이러닝\[큐레이팅# 플러스] 최적의 코딩을 결정하는 기본 알고리즘\image\2-6.PNG)

## 힙에 원소가 제거될 때 

* 원소가 제거되었을때, O(logN)의 시간 복잡도로 힙 성질을 유지하도록 할 수 있습니다.
* 원소를 제거할 떄는 가장 마지막 노드가 루트 노드의 위치에 오도록 합니다.

![2-7](C:\Users\여름\Desktop\학습자료\이러닝\[큐레이팅# 플러스] 최적의 코딩을 결정하는 기본 알고리즘\image\2-7.PNG)

* 이후에 루트 노드에서부터 하향식으로(더 작은 자식 노드로) Heapify() 를 진행합니다.

![2-8](C:\Users\여름\Desktop\학습자료\이러닝\[큐레이팅# 플러스] 최적의 코딩을 결정하는 기본 알고리즘\image\2-8.PNG)



## 우선순위 큐 라이브러리를 활용한 힙 정렬 구현 예제

```python
import sys
import heapq
input = sys.stdin.readline()

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))
    
res = heapsort(arr)

for i in range(n):
    print(res[i])
```

