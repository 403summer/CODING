# [기초-산술연산] 정수 2개 입력받아 나눈 나머지 계산하기

[문제링크](https://codeup.kr/problem.php?id=6041)



## 1. 문제설명

정수 2개(a, b) 를 입력받아 a를 b로 나눈 나머지를 출력해보자.




## 2. 문제풀이

```python
a, b = input().split()
c = int(a)%int(b)
print(c)
```



## 3. 참고

python 언어에서는 나눈 나머지를 계산하는 연산자(%, remainder)를 제공한다.
a%b 와 같이 작성하면, a를 b로 나눈 나머지(remainder)를 계산해준다.
나머지 연산(modulus, mod 연산)은 수학자 가우스가 생각해 낸 연산으로,
어떤 수를 다른 수로 나누고 난 후 남는 나머지를 계산하는 연산이다.

