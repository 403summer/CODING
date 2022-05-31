# [기초-입출력] 시분초 입력받아 분만 출력하기

[문제링크](https://codeup.kr/problem.php?id=6023)



## 1. 문제설명

시:분:초 형식으로 시간이 입력될 때 분만 출력해보자.




## 2. 문제풀이

```python
# 방법 1
h, m, s = input().split(':')
print(m)

# 방법 2
time = input().split(':')
print(time[1])
```



