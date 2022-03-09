import heapq
import sys
input = sys.stdin.readline
n = int(input())
data = []
for i in range(n):
  heapq.heappush(data, int(input()))
  
result = 0
while len(data) > 1:
  fir = heapq.heappop(data)
  sec = heapq.heappop(data)
  heapq.heappush(data, fir+sec)
  result += fir + sec

print(result)
