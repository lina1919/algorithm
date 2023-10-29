n = int(input())
arr = []
dict = {}

for _ in range(n):
  a = str(input())
  for i in range(len(a)):
    if a[i] in dict:
      dict[a[i]] += 10**(len(a)-i-1)
    else:
      dict[a[i]] = 10**(len(a)-i-1)
  arr.append(a)
dict_sorted = sorted(dict.items(), key=lambda item: item[1], reverse=True)
sum = 0
pows = 9
for num in dict_sorted:
  sum += pows*num[1]
  pows -= 1
print(sum)
