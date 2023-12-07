def get_permutations(s, start=0):
  if start == len(s) - 1:
      return [s]

  permutations = []
  for i in range(start, len(s)):
      # i번째 문자와 start 위치의 문자를 교환
      chars = list(s)
      chars[start], chars[i] = chars[i], chars[start]
      swapped_str = ''.join(chars)

      # 나머지 부분에 대해 순열을 구하고 현재 위치의 문자와 합치기
      remaining_permutations = get_permutations(swapped_str, start + 1)
      permutations.extend(remaining_permutations)

  return permutations

# 테스트
x = input()
result = get_permutations(x)
result.sort()
findFlag = False
for r in result:
  if int(r) > int(x):
    print(int(r))
    findFlag = True
    break
if findFlag == False:
  print(0)

# 재귀로 푸는 풀이
  #이게 더 나은듯..?
  
# x=list(input())
# n=len(x)
# ans=1000000
# check=[False]*n

# def go(num,k):
#     if k==n:
#         if num>int(''.join(x)):
#             global ans
#             ans=min(ans,num)
#         return
#     for i in range(n):
#         if check[i]==False:
#             check[i]=True
#             go(num*10+int(x[i]),k+1)
#             check[i]=False

# go(0,0)
# print(0 if ans==1000000 else ans)
