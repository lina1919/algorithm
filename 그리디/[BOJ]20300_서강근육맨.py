n = int(input())
#각 운동기구의 근손실 정도
T = list(map(int, input().split()))
T.sort()
l = len(T)
sum = 0
if l%2==0:
  #반씩더하니까 반까지만 하면 됨
  for i in range(l//2):
    s = T[i] + T[l-i-1]
    #최대값을 구해야함
    sum = max(s,sum)
else:
  for i in range(l//2-1):
    s = T[i] + T[l-i-2]
    sum = max(s,sum)
  sum = max(sum,T[l-1])
print(sum)
