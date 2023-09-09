#우와 이거 한번에 맞췄다!
# 이렇게 푸는 방법이 맞다 dfs로
# 부루트포스, 백트래킹

import sys

input = sys.stdin.readline

#1e9
minK = 1000000000

sour = 0
sweet = 0

def dfs(x,k):
  global minK
  sour = 1
  sweet = 0
  if len(a) == k:
    for x in a:
      sour *= arr[x][0]
      sweet += arr[x][1]
      minK = min(abs(sour-sweet), minK)
    return
  for i in range(x,n):
    if i not in a:
      a.append(i)
      dfs(i,k)
      a.pop()
      
a = []
n = int(input())
arr = []
for _ in range(0,n):
  temp = []
  temp = list(map(int, input().split()))
  arr.append(temp)

for i in range(0,n):
  dfs(0,i+1)

print(minK)
    
# itertools를 사용한하니 더 간단해진다
# import sys, itertools
# from itertools import combinations
# input = sys.stdin.readline

# n = int(input())
# sour = []
# bitter = []
# for _ in range(n):
#     a, b = map(int, input().split())
#     sour.append(a)
#     bitter.append(b)

# diff = float('inf')

# for i in range(1, n+1): # 재료를 i개 뽑을 때
#     idxs = list(combinations(list(range(n)), i)) # 가능한 경우를 담은 리스트

#     for food in idxs: # 경우 하나씩 탐색
#         s = 1
#         b = 0

#         for j in range(i): # 맛 계산
#             s *= sour[food[j]]
#             b += bitter[food[j]]
#         if abs(s - b) < diff:
#             diff = abs(s - b)

# print(diff)
