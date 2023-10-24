def check_if_sub(str1, str2):
  for i in range(len(str1)):
    if(str1[i] != str2[i]):
        return False
  return True

count = int(input())
arr = []
for _ in range(count):
  arr.append(str(input()))

#문자열 크기에 따른 정렬
arr.sort(key=len)
sub = 0
answer = 0
for i in range(count):
  flag = False
  for j in range(i+1,count):
    if(check_if_sub(arr[i], arr[j])):
      flag = True
      break
  #얘네는 접두사가 아니니 정답에 더해라
  if flag == False:
    answer += 1

print(answer)
