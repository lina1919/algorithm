from collections import deque
import sys

sys.setrecursionlimit(1000000)
m,n,k = map(int,input().split())

dx = [0,0,1,-1]
dy = [1,-1,0,0]
visit = []
arr = []
ans = []

for i in range(n):
  arr.append([False]*m)
  visit.append([False]*m)
  
for _ in range(k):
  x1,y1,x2,y2 = map(int,input().split())
  for i in range(x1,x2):
    for j in range(y1,y2):
      arr[i][j] = True

def bfs(s1,s2):
  answer = 1
  visit[s1][s2] = True
  q = deque()
  q.append([s1,s2])
  while q:
    x,y = q.popleft()
    for i in range(4):
      nextx = x + dx[i]
      nexty = y + dy[i]
      if nextx < n and nexty < m and nextx >= 0 and nexty >= 0:
        if not visit[nextx][nexty] and not arr[nextx][nexty]:
          visit[nextx][nexty] = True
          answer += 1
          q.append([nextx,nexty])
  return answer

count = 0

def dfs(x,y):
  
  visit[x][y] = True
  global count
  count += 1
  for i in range(4):
    nextx = x + dx[i]
    nexty = y + dy[i]
    if nextx < n and nexty < m and nextx >= 0 and nexty >= 0:
      if not visit[nextx][nexty] and not arr[nextx][nexty]:
        dfs(nextx,nexty)
  
for i in range(n):
  for j in range(m):
    if visit[i][j] == False and arr[i][j] == False:
      dfs(i,j)
      ans.append(count)
      count = 0

ans.sort()
print(len(ans))
for k in ans:
  print(k,end=" ")
          
          
    
