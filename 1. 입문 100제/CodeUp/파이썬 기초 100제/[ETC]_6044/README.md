# [기초-산술연산] 정수 2개 입력받아 자동 계산하기

[문제링크](https://codeup.kr/problem.php?id=6044)



## 1. 문제설명

정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산해보자.
단, b는 0이 아니다.




## 2. 문제풀이

```python
a, b = input().split()
a = int(a)
b = int(b)
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(format(a/b,'.2f'))
```


