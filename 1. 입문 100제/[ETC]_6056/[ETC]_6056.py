#[기초-논리연산] 참/거짓이 서로 다를 때에만 참 출력하기

c, d = input().split()
c = bool(int(c))
d = bool(int(d))
print((c and (not d)) or ((not c) and d))
