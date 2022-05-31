# [기초-입출력] 주민번호 입력받아 형태 바꿔 출력하기

[문제링크](https://codeup.kr/problem.php?id=6020)



## 1. 문제설명

주민번호는 다음과 같이 구성된다.
XXXXXX-XXXXXXX

왼쪽 6자리는 생년월일(YYMMDD)이고, 오른쪽 7자리는 성별,출생지역,확인코드로 구성되어있다.
주민번호를 입력받아 형태를 바꿔 출력해보자.




## 2. 문제풀이

```python
front, back = input().split('-')
print(front, back, sep="")
```



