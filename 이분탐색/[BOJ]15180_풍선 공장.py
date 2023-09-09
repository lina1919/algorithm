n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
start = arr[0]
end = start * m

while (start != end):
  cnt = 0
  mid = (start + end)//2
  for i in range(n):
    cnt += mid // arr[i]
    if(cnt >= m): 
      break
  if(cnt>=m):
    end = mid
  else:
    start = mid +1

print(end)
