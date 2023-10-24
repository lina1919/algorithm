count = int(input())
arr = list(map(int, input().split()))

arr.sort()

if count%2==0:
  print(arr[count//2-1])
else:
  print(arr[count//2])
#실패한 풀이
#그냥 단순하게 생각했어야 함. 가운데 있는 애가 제일 최소가 되는 값이다.
# distance = 0
# answer = 1111111111
# index = 1111111111

# for i in range(count):
#   distance = 0
#   for j in range(0, count):
#     distance += abs(arr[j] - arr[i])
#     if distance >= answer:
#       continue
#   if distance < answer:
#     answer = distance
#     index = i

# print(arr[index])
