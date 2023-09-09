import sys

input = sys.stdin.readline

arr = []
cnt = 0

n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

var = arr[n-1]

for i in range(0,n+1):
  if k>=var:
    cnt += k // var
    if k%var == 0:
      break
    k = k % var
    if i == n+1 :
      break
    # 1인 경우를 고려하지 않아서 틀렸다
  var = arr[n-1-i]

print(cnt)
      
