#비트마스크

import sys
input = sys.stdin.readline
MAX = 1e9

n = int(input())
ingres = [tuple(map(int, input().split())) for _ in range(n)]

answer = MAX
for set in range(1, 1 << n):
  s = 1
  b = 0
  for j in range(n):
    if (set & (1 << j)) != 0:
      s *= ingres[j][0]
      b += ingres[j][1]
  answer = min(answer, abs(s - b))
print(answer)
