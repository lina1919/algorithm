from collections import deque
 
dx = [0,0,1,-1]
dy = [1,-1,0,0]

count = 0

def bfs(graph, a, b):
  n = len(graph)
  queue = deque()
  #파이썬은 이것도 쌉가능이군..
  #queue<pair<int, int>>q; q.push({ y,x }); 아 c++도 가능이군..
  queue.append((a,b))
  graph[a][b] = 0
  count = 1

  while queue:
    x,y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= n:
        continue
      if graph[nx][ny] == 1:
        graph[nx][ny] = 0
        queue.append((nx,ny))
        count += 1
  return count

def dfs(graph, x, y):
    global count
    if x < 0 or x >= n or y < 0 or y >= n:
        return
    #visited 대신 graph에 바로 표시
    if graph[x][y] == 1:
        count += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(graph, nx, ny)
    

n = int(input())
graph = []
for _ in range(n):
  graph.append(list(map(int,input())))
cnt = []

#dfs
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            dfs(graph, i, j)
            cnt.append(count)
            count = 0

#bfs
# for i in range(n):
#   for j in range(n):
#     if graph[i][j] == 1:
#       cnt.append(bfs(graph, i, j))

cnt.sort()
print(len(cnt))
for i in range((len(cnt))):
  print(cnt[i])
