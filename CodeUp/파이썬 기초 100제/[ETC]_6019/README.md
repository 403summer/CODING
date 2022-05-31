# [기초-입출력] 연월일 입력받아 순서 바꿔 출력하기

[문제링크](https://codeup.kr/problem.php?id=6019)



## 1. 문제설명

"연도.월.일"을 입력받아 "일-월-연도" 순서로 바꿔 출력해보자.




## 2. 문제풀이

```python
year, month, day = input().split('.')
print(day, month, year, sep='-')
```



