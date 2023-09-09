import math,sys
input = sys.stdin.readline

n,c = map(int, input().split())
arr = []           
for i in range(n):
  arr.append(int(input()))
arr.sort()
start = 1
end = arr[-1] - arr[0]
answer = 0

while (start <= end):
  #이미 한 개 두고 시작하는 것이기 때문에
  cnt = 1
  mid = (start + end)//2
  k = arr[0]
  for i in range(1,len(arr)):
    if(arr[i] >= k + mid):
      cnt+=1
      k=arr[i]
  if(cnt<c):
    end = mid - 1
  else:
    start = mid + 1
    answer = mid
print(answer)
