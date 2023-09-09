import math,sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
S = int(input())

i=0

while S>0 and i<N:
  m = arr.index(max(arr[i:i+S+1]))
  if m!=i:
    arr[m], arr[m-1] = arr[m-1], arr[m]
    S-=1
  else:
    i+=1
  
print(*arr)
    
