# [기초-산술연산] 정수 3개 입력받아 합과 평균 출력하기

[문제링크](https://codeup.kr/problem.php?id=6045)



## 1. 문제설명

정수 3개를 입력받아 합과 평균을 출력해보자.




## 2. 문제풀이

```python
a, b, c =input().split()
d = int(a)+int(b)+int(c)
e = format(float(d)/3.0,'.2f')
print(d, e)
```


