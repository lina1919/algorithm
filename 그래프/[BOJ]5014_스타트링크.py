from collections import deque

f,s,g,u,d = map(int,input().split())
visit = [False]*(f+1)
dist = [0]*(f+1)

def bfs():
  visit[s]=True
  q=deque([s])
  while q:
    now = q.popleft()
    if now == g:
      return dist[g]
      
    next = now + u
    if next <= f and not visit[next]:
      visit[next] = True
      dist[next] = dist[now] + 1
      q.append(next)
      
    next = now - d
    if next >= 1 and not visit[next]:
      visit[next] = True
      dist[next] = dist[now] + 1
      q.append(next)
  return "use the stairs"
  
print(bfs())
