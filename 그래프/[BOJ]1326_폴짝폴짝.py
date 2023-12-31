from collections import deque

n = int(input())
l = [0]+list(map(int,input().split()))
a,b = map(int,input().split())
visit = [False]*(n+1)
dist = [0]*(n+1)

def bfs():
  visit[a]=True
  q=deque([a])
  while q:
    now = q.popleft()
    if now == b:
      return dist[b]
    for next in range(now,n+1,l[now]):
      if not visit[next]:
        visit[next] = True
        dist[next] = dist[now] + 1
        q.append(next)
    for next in range(now,0,-l[now]):
      if not visit[next]:
        visit[next] = True
        dist[next] = dist[now] + 1
        q.append(next)
  return -1
print(bfs())
