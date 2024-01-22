n = int(input())
d = [0]*(11)
d[1] = 1
d[2] = 2
d[3] = 4

#bottom-up(iterative),반복문
# for j in range(1,14):
#   if j == 1:
#     dp[j] = 1
#   elif j == 2:
#     dp[j] = 2
#   elif j == 3:
#     dp[j] = 4
#   else:
#     dp[j] = dp[j-1] + dp[j-2] + dp[j-3]

#top-down(recursive) 재귀
def dp(n):
  if n<4 or d[n]:
    return d[n]
  d[n] = dp(n-1)+dp(n-2)+dp(n-3)
  return d[n]
  
for i in range(n):
  num = int(input())
  print(dp(num))
