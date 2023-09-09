k, n = map(int, input().split())
arr = []           
for i in range(k):
  arr.append(int(input()))
arr.sort()
#최초 start를 1로 바꾸니 해결
start = 1
end = arr[-1]
while (start <= end):
  cnt = 0
  mid = (start + end)//2
  for i in arr:
    cnt += i // mid
  if(cnt<n):
    end = mid - 1
  else:
    start = mid + 1
    
print(end)
