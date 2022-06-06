#[기초-논리연산] 하나라도 참이면 참 출력하기

a, b = input().split()
print(bool(int(a)) or bool(int(b)))
