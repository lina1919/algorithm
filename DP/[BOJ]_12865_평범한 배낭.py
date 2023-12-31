#낵셉 배낭 문제
n, k = map(int,input().split())

d = [[0]*(k+1) for _ in range(n+1)]
arr = []
for _ in range(n):
   arr.append(list(map(int,input().split())))
  
for i in range(1, n+1):
  for j in range(1, k+1):
      w = arr[i-1][0]
      v = arr[i-1][1]
      if j < w:
          d[i][j] = d[i-1][j]
      else:
          d[i][j] = max(d[i-1][j], d[i-1][j-w]+v)

print(d[n][k])
