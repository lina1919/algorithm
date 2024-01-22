n = int(input())
a = 1
for i in range(2,n+1):
  a *= i
  while a%10==0:
    a//=10
  a%=1000000000000
a = str(a)
print(a[-5:])
