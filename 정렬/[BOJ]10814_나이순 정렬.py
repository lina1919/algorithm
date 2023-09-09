import sys

input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(0,n):
  arr.append(list(input().split()))
#각 원소의 첫 번째 요소를 정수로 변환한 값에 따라 리스트가 정렬
arr.sort(key=lambda x:int(x[0]))

for i in range(0,n):
  print(arr[i][0] + " " + arr[i][1])
