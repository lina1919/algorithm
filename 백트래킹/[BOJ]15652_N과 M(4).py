#중복조합 백트래킹-dfs의 일종
import sys

input = sys.stdin.readline

def dfs(x):
  if len(arr)==m:
    print(*arr)
    return
  for i in range(x,n+1):
    arr.append(i)
    dfs(i)
    arr.pop()
    
n,m = map(int, input().split())
arr = []
dfs(1)


