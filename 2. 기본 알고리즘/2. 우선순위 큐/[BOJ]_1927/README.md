# [BOJ-1927] 최소 힙 

[문제링크](https://www.acmicpc.net/problem/1927)



## 1. 문제유형

* 자료구조
* 우선순위 큐



## 2. 문제설명

널리 잘 알려진 자료구조 중 최소 힙이 있다. 최소 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.

1. 배열에 자연수 x를 넣는다.
2. 배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.

프로그램은 처음에 비어있는 배열에서 시작하게 된다.




## 3. 문제풀이

```python
import sys
import heapq

N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for i in range(N)]
h = []
result = []
for i in nums:
    if i != 0:
        heapq.heappush(h, i)
    else:
        if len(h) == 0:
            result.append(0)
        else:
            result.append(heapq.heappop(h))
for j in result:
    print(j)
```


