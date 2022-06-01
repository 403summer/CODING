# [기초-출력변환] 10진 정수 입력받아 16진수로 출력하기2

[문제링크](https://codeup.kr/problem.php?id=6028)



## 1. 문제설명

10진수를 입력받아 16진수(hexadecimal)를 대문자로 출력해보자.




## 2. 문제풀이

```python
a = input()
n = int(a)
print('%X' %n)
```



## 3. 참고

10진수 형태로 입력받고
%X로 출력하면 16진수(hexadecimal)대문자로 출력된다.

