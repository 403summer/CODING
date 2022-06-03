#[기초-산술연산] 정수 3개 입력받아 합과 평균 출력하기

a, b, c =input().split()
d = int(a)+int(b)+int(c)
e = format(float(d)/3.0,'.2f')
print(d, e)
