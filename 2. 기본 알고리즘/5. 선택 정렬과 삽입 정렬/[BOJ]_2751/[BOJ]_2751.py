#[BOJ-2751] 수 정렬하기 2
import sys
N = int(sys.stdin.readline())
array = [int(sys.stdin.readline()) for i in range(N)]
array.sort()
for i in array:
    print(i)

