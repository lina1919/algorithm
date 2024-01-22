n = int(input())
cnt = 0
for _ in range(n):
  flag = False
  s = input()
  set = []
  set.append(s[0])
  start = s[0]
  if len(s) == 1:
    cnt += 1
    continue
  for i in range(1, len(s)):
    if s[i] in set and start != s[i]:
      flag = True
      break
    if s[i] not in set:
      set.append(s[i])
      start = s[i]
  if flag == False:
    cnt += 1
print(cnt)
      
