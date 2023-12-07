import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)

ans = arr[0]
for i in range(1,n):
  ans += arr[i]/2

print(ans)
