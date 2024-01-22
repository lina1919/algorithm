s,c = map(int,input().split())
pa = []
for _ in range(s):
  pa.append(int(input()))

pa.sort()

low , high = 1 , pa[-1]
while low<=high:
  cnt = 0
  mid = (low+high)//2
  for i in pa:
    cnt += i // mid
  if cnt < c:
    high = mid -1
  else:
    low = mid +1
ans = 0

print(sum(pa)-high*c)
