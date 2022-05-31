#[기초-입출력] 시분초 입력받아 분만 출력하기

# 방법 1
h, m, s = input().split(':')
print(m)

# 방법 2
time = input().split(':')
print(time[1])