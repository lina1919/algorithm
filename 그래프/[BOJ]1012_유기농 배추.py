import sys
#이거 안넣으면 runtime error 발생
sys.setrecursionlimit(10000)
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(arr, a, b):
  if arr[b][a] == 1:
    arr[b][a] = 0
    for i in range(4):
      na = a + dx[i]
      nb = b + dy[i]
      if na < 0 or na>=m or nb<0 or nb>=n:
        continue
      
      if arr[nb][na] == 1:
        dfs(arr,na,nb)
        
t = int(input())
for _ in range(t):
  #m 가로 n 세로 배추 개수 k
  m,n,k = map(int, input().split())
  arr = [[0 for j in range(m)] for i in range(n)]
  for _ in range(k):
    x,y = map(int, input().split())
    #둘이 순서 바꿔줘야함(<가로,세로> 순서이기 때문에)
    arr[y][x] = 1
  count = 0
  #이중 반복문 돌 때 가로부터
  for i in range(m):
    for j in range(n):
      #여기도 마찬가지
      if arr[j][i] == 1:
        count += 1
        dfs(arr,i,j)   
  print(count)
