h,w,x,y = map(int, input().split())
# 2 4 1 1
# h x w 배열 A
# (H + X) × (W + Y)인 배열 B
# 아래로 x칸 오른쪽으로 y칸

b = [list(map(int, input().split())) for _ in range(h+x)]
a = [[0]*w for _ in range(h)]

for i in range(h):
  for j in range(w):
      if i<x or i>=h or j<y or j>=w:
          a[i][j]=b[i][j]
      else:
          a[i][j] = b[i][j]-a[i-x][j-y]

for arr in a:
  print(*arr)
