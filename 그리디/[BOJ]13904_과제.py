n = int(input())
arr = []
for i in range(n):
  a = list(map(int, input().split()))
  arr.append(a)

max_d = 0
for i in range(n):
  if max_d < arr[i][0]:
      max_d = arr[i][0]
days = [0] * max_d

arr.sort(key=lambda x: -x[1])

for a in arr:
  for i in range(a[0]-1,-1,-1):
    if days[i] == 0:
      days[i] = a[1]
      break

print(sum(days))
