m,n = map(int,input().split())

arr = [False,False] + [True] *(n+1)

prime = []

for i in range(2,n+1):
  if arr[i]:
    prime.append(i)
    for j in range(2*i,n+1,i):
      arr[j] = False

for p in prime:
  if p >= m:
    print(p)
