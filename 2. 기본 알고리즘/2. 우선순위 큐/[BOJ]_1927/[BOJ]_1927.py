#[BOJ-1927] 최소 힙
import sys
import heapq

N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for i in range(N)]
h = []
result = []
for i in nums:
    if i != 0:
        heapq.heappush(h, i)
    else:
        if len(h) == 0:
            result.append(0)
        else:
            result.append(heapq.heappop(h))
for j in result:
    print(j)


