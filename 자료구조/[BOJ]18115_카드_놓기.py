import sys
from collections import deque

# 덱 생성
d = deque()
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
arr.reverse()

for i in range(n):
  if arr[i] == 1:
    d.appendleft(i+1)
  elif arr[i] == 3:
    d.append(i+1)
  elif arr[i] == 2:
    d.insert(1,i+1)

for a in d:
  print(a,end=" ")
    
