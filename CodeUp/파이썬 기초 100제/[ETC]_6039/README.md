# [기초-산술연산] 실수 2개 입력받아 거듭제곱 계산하기

[문제링크](https://codeup.kr/problem.php?id=6039)



## 1. 문제설명

실수 2개(f1, f2)를 입력받아
f1을 f2번 거듭제곱한 값을 출력하는 프로그램을 작성해보자.




## 2. 문제풀이

```python
f1, f2 = input().split()
f = float(f1)**float(f2)
print(f)
```



