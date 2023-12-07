from collections import deque

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
m = int(input())
C = list(map(int, input().split()))

result = []
queue = deque()
for i in range(n):
  if A[i] == 0:
    queue.appendleft(B[i])

for i in range(m):
  queue.append(C[i])
  print(queue.popleft(), end=' ')
