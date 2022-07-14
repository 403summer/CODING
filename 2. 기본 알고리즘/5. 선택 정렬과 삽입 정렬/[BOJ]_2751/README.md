# [BOJ-2751] 수 정렬하기 2 

[문제링크](https://www.acmicpc.net/problem/2751)



## 1. 문제유형

* 정렬

## 2. 문제설명

첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.


## 3. 문제풀이

```python
import sys
N = int(sys.stdin.readline())
array = [int(sys.stdin.readline()) for i in range(N)]
array.sort()
for i in array:
    print(i)
```


