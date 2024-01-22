import sys
import math
input = sys.stdin.readline
n,m = map(int,input().split())
arr = list(map(int,input().split()))
sum = 0
for i in range(m):
  sum += arr[i]
max = sum
for i in range(m,n):
  sum = sum - arr[i-m]
  sum += arr[i]
  if max < sum:
    max = sum
print(max)
