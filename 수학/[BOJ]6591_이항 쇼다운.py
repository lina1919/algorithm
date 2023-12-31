import sys
import math
input = sys.stdin.readline
while True:
  n,k = map(int,input().split())
  if n==0 and k==0:
    exit()
  print(math.comb(n,k))
