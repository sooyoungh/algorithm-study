# 그래프에 저장하면서 나아가기, 마지막 열에서 최대가 답
# 중간지점에서 최대가 최종결과값 최대가 아닐수도 있음! => 계속 저장하면서 최종 최대값 구하기!!
n, m = map(int, input().split())
data = list(map(int, input().split()))
index = 0
graph = []
for i in range(n):
  graph.append(data[index:index + m])
  index += m

result = []

for i in range(1, m):
  for j in range(n):
    target = graph[j][i]
    if j-1 <0:
      fir = 0
    else:
      fir = graph[j-1][i-1] + target
      
    if j+1 > n-1:
      thr = 0
    else:
      thr = graph[j+1][i-1] + target
    sec = graph[j][i-1] + target
    graph[j][i] = max(fir,sec,thr)

print(graph)
arr = []
for i in range(n):
  arr.append(graph[i][m-1])
print(max(arr))
