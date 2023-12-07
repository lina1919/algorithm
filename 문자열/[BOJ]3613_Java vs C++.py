word = input()
l = len(word)
is_java = False
is_C = False
if '_' in word:
  is_C = True
for a in word:
  if a.isupper():
    is_java = True
    
if is_java == True and is_C == True:
  print("Error!")
  exit()

#문자열 자체에서 파싱하다가 index out of range 오류 다량 발생
#그냥 빈 문자열 만들고 거기에 추가하는게 나을듯
elif is_java:
  i = 0
  ans = ''
  while i<l:
    if word[i].isupper():
      if i==0:
        print("Error!")
        exit()
      ans += '_'
      ans += word[i].lower()
    else:
      ans+=word[i]
    i+=1
  print(ans)
else:
  i = 0
  ans = ''
  while i<l:
    if word[i] == '_':
      if i==0 or i==l-1 or (i+1<l and word[i+1]=='_'):
        print("Error!")
        exit()
      ans += word[i+1].upper()
      i+=1
    else:
      ans+=word[i]
    i+=1
  print(ans)
