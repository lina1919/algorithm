num = int(''.join(input().split()))

#시계수 찾기
def find(num):
  a = num
  for i in range(3):
    #숫자 순열 구하는 간단한 방법
    num = (num%1000) * 10 + num//1000
    if a > num:
      a = num
  return a

start = 1111
cnt = 0
num = find(num)
while(start<=num):
  if '0' in str(num):
    continue
  if find(start) == start:
    cnt += 1
  start += 1
  
print(cnt)
  
